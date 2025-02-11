from sqlalchemy.ext.asyncio import AsyncSession

from repositories.base_uow import UnitOfWork
from infrastructure.sqlalchemy.user_repo import UserSQLAlchemyRepository
from infrastructure.sqlalchemy.account_repo import AccountSQLAlchemyRepository
from infrastructure.sqlalchemy.transaction_repo import (
    TransactionSQLAlchemyRepository
)


class SQLAlchemyUnitOfWork(UnitOfWork):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session
        self.user_repo = UserSQLAlchemyRepository(session)
        self.account_repo = AccountSQLAlchemyRepository(session)
        self.transaction_repo = TransactionSQLAlchemyRepository(session)

    async def __aenter__(self) -> None:
        await self._session.begin()
    
    async def __aexit__(self, exc_type, exc_value, traceback) -> None:
        if exc_type:
            self.rollback()
        else:
            self.commit()
    
    async def rollback(self) -> None:
        await self._session.rollback()
    
    async def commit(self) -> None:
        await self._session.commit()
        