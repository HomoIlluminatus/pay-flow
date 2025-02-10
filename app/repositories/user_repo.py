from abc import ABC, abstractmethod

from domain.user import User
from .base_repo import AbstractRepository


class UserRepository(AbstractRepository[User]):
    @abstractmethod
    async def get_user_by_email(self, email: str) -> User:
        ...
        