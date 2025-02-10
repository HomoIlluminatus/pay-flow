from dataclasses import dataclass
from uuid import UUID

from .base_error import BaseAppError


@dataclass
class TransactionError(BaseAppError):
    @property
    def message(self) -> str:
        return "Transaction error"


@dataclass
class TransactionNotFoundError(TransactionError):
    transaction_id: UUID
    
    @property
    def message(self) -> str:
        return f"Transaction not found: id {self.transaction_id}"


@dataclass
class TransactionExistError(TransactionError):
    transaction_id: UUID
    
    @property
    def message(self):
        return f"Transaction already exists: id {self.transaction_id}"
    