from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID

from errors.base_error import BaseAppError


@dataclass
class AccountError(BaseAppError):
    @property
    def message(self) -> str:
        return "Account error"


@dataclass
class InvalidDepositAmountError(AccountError):
    amount: Decimal

    @property
    def message(self) -> str:
        return f"The deposit amount must be positive. Specified: {self.amount}"


@dataclass
class InvalidWithdrawalAmountError(AccountError):
    amount: Decimal

    @property
    def message(self) -> str:
        return (
            f"The withdrawal amount must be greater than zero."
            f" Specified: {self.amount}"
        )


@dataclass
class InsufficientFundsError(AccountError):
    amount: Decimal
    balance: Decimal

    @property
    def message(self) -> str:
        return (
            f"Payment error: insufficient funds."
            f" Balance: {self.balance}, Requested: {self.amount}"
        )


@dataclass
class AccountNotFoundError(AccountError):
    account_id: UUID

    @property
    def message(self) -> str:
        return f"Account not found: ID {str(self.account_id)}"
