from typing import List
from uuid import UUID

from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from domain.account import Account
from repositories.account_repo import AccountRepository
from .base_repo import BaseSQLAlchemyRepository


class AccountSQLAlchemyRepository(BaseSQLAlchemyRepository[Account],
                               AccountRepository):
    async def get_user_accounts_list(self, user_id: UUID) -> List[Account]:
        result = await self._session.execute(
            select(Account).where(Account.user_id == user_id)
        )
        return result.scalars().all()
    
    async def delete_user_all_accounts(self, user_id) -> None:
        await self._session.execute(
            delete(Account).where(Account.user_id == user_id)
        )
        await self._session.commit()
        