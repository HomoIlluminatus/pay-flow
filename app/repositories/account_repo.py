from abc import ABC, abstractmethod
from typing import List
from uuid import UUID

from domain.account import Account

from repositories.base_repo import AbstractRepository


class AccountRepository(ABC, AbstractRepository):
    @abstractmethod
    async def get_user_accounts_list(self, user_id: UUID) -> List[Account]:
        ...
        