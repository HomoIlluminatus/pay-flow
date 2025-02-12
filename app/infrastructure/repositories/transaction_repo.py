from typing import List, Optional
from uuid import UUID

from sqlalchemy import delete
from sqlalchemy.future import select

from domain.transaction import Transaction
from repositories.transaction_repo import TransactionRepository
from .base_repo import BaseSQLAlchemyRepository


class TransactionSQLAlchemyRepository(BaseSQLAlchemyRepository[Transaction],
                               TransactionRepository):
    async def get_account_transactions_list(
        self,
        account_id: UUID
    ) -> List[Transaction]:
        result = await self._session.execute(
            select(self._model).where(self._model.account_id == account_id)
        )
        return result.scalars().all()
    
    async def get_user_transactions_list(
        self,
        user_id: UUID        
    ) -> List[Transaction]:
        result = await self._session.execute(
            select(self._model).where(self._model.user_id == user_id)
        )
        return result.scalars().all()
    
    async def delete_account_all_transactions(self, account_id):
        await self._session.execute(
            delete(self._model).where(self._model.account_id == account_id)
        )
        await self._session.commit()
        
    async def delete_user_all_transactions(self, user_id) -> None:
        await self._session.execute(
            delete(self._model).where(self._model.user_id == user_id)
        )
        await self._session.commit()
        