from typing import Optional
from uuid import UUID

from core.errors.user_errors import UserExistError, UserNotFoundError
from domain.user import User
from repositories.base_uow import UnitOfWork


class UserService:
    def __init__(self, uow: UnitOfWork) -> None:
        self._uow = uow
        
    async def get_user_or_raise(self, user_id: UUID) -> User:
        user = await self._uow.user_repo.get_by_id(user_id)
        if user is None:
            raise UserNotFoundError(user_id)
        return user
    
    async def get_user_by_email(self, email: str) -> Optional[User]:
        return await self._uow.user_repo.get_user_by_email(email)
    
    async def get_users_list(self):
        return await self._uow.user_repo.get_list()
        
    async def create_user(self, user: User) -> User:
        async with self._uow:
            existing_user = await self._uow.user_repo.get_user_by_email(
                user.email
            )
            if existing_user is not None:
                raise UserExistError(user.email)
            await self._uow.user_repo.add(user)
            await self._uow.commit()
            return user
        
    async def update(self, user: User) -> User:
        async with self._uow:
            await self._uow.user_repo.update(user)
            await self._uow.commit()
            return user
        
    async def delete(self, user_id: UUID) -> None:
        async with self._uow:
            await self._uow.user_repo.delete(user_id)
            await self._uow.commit()
            