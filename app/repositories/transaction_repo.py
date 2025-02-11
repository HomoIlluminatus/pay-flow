from abc import ABC, abstractmethod
from typing import List
from uuid import UUID

from domain.transaction import Transaction
from .base_repo import AbstractRepository


class TransactionRepository(AbstractRepository[Transaction]):
    @abstractmethod
    async def get_account_transactions_list(
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
        
    @abstractmethod
    async def delete_user_all_transactions(self, user_id: UUID) -> None:
        ...
        
    @abstractmethod
    async def delete_account_all_transactions(self, account_id: UUID) -> None:
        ...
        