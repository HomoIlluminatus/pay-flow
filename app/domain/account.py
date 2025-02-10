from dataclasses import dataclass, field
from decimal import Decimal
from uuid import UUID

from domain.base_entity import BaseEtity
from core.errors.account_errors import InsufficientFundsError
from core.errors.account_errors import InvalidDepositAmountError
from core.errors.account_errors import InvalidWithdrawalAmountError


@dataclass
class Account(BaseEtity):
    user_id: UUID
    balance: Decimal = field(default=0.0)
    
    def deposit(self, amount: Decimal) -> None:
        if amount <= 0:
            raise InvalidDepositAmountError(amount)
        self.balance += amount
        
    def withdrow(self, amount: Decimal) -> None:
        if amount <= 0:
            raise InsufficientFundsError(amount, self.balance)
        
        if amount > self.balance:
            raise InvalidWithdrawalAmountError(amount)
        
        self.balance -= amount
        