from abc import ABC, abstractmethod

from .account_repo import AccountRepository
from .transaction_repo import TransactionRepository
from .user_repo import UserRepository


class UnitOfWork(ABC):
    user_repo: UserRepository
    account_repo: AccountRepository
    transaction_repo: TransactionRepository
    
    @abstractmethod
    async def __aenter__(self):
        ...
    
    @abstractmethod
    async def __aexit__(self, exc_type, exc_value, traceback):
        ...
    
    @abstractmethod
    async def commit(self):
        ...
    
    @abstractmethod
    async def rollback(self):
        ...
