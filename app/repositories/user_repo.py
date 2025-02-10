from abc import ABC, abstractmethod

from domain.user import User
from repositories.base_repo import AbstractRepository


class UserRepository(ABC, AbstractRepository[User]):
    @abstractmethod
    async def get_user_by_email(self, email: str) -> User:
        ...
        