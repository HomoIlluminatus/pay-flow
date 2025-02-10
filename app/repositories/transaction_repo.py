from abc import ABC, abstractmethod
from typing import List
from uuid import UUID

from domain.transaction import Transaction
from .base_repo import AbstractRepository


class TransactionRepository(AbstractRepository):
    @abstractmethod
    async def get_accounts_transactions_list(
        self,
        account_id: UUID
    ) -> List[Transaction]:
        ...
    
    @abstractmethod
    async def get_user_transactions_list(
        self,
        user_id: UUID
    ) -> List[Transaction]:
        ...
        