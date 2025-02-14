from abc import ABC, abstractmethod
from typing import List
from uuid import UUID

from domain.account import Account

from .base_repo import AbstractRepository


class AccountRepository(AbstractRepository[Account]):
    @abstractmethod
    async def get_user_accounts_list(self, user_id: UUID) -> List[Account]:
        ...
    
    @abstractmethod
    async def delete_user_all_accounts(self, user_id: UUID) -> None:
        ...