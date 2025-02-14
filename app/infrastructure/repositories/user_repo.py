from typing import List, Optional
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from domain.user import User
from repositories.user_repo import UserRepository
from .base_repo import BaseSQLAlchemyRepository


class UserSQLAlchemyRepository(BaseSQLAlchemyRepository[User], UserRepository):    
    async def get_user_by_email(self, email: str) -> Optional[User]:
        result = await self._session.execute(
            select(self._model).where(self._model.email == email)
        )
        return result.scalars().first()
    