from typing import List
from uuid import UUID

from core.errors.account_errors import AccountNotFoundError
from core.errors.transaction_errors import TransactionNotFoundError
from core.errors.user_errors import UserNotFoundError
from domain.account import Account
from domain.transaction import Transaction
from repositories.base_uow import UnitOfWork


class TransactionService:
    def __init__(self, uow: UnitOfWork) -> None:
        self._uow = uow
        
    async def get_transaction_or_raise(
        self,
        transaction_id: UUID
    ) -> Transaction:
        transaction = await self._uow.transaction_repo.get_by_id(transaction_id)
        if transaction is None:
            raise TransactionNotFoundError(transaction_id)
        return transaction
    
    async def get_transacions_list(self) -> List[Transaction]:
        return await self._uow.transaction_repo.get_list()
    
    async def get_account_transactions_list(
        self,
        account_id: UUID
    ) -> List[Transaction]:
        existing_account = await self._uow.account_repo.get_by_id(account_id)
        if existing_account is None:
            raise AccountNotFoundError(account_id)
        return await self._uow.transaction_repo.get_accounts_transactions_list(
            account_id
        )
    
    async def get_user_transactions_list(self, user_id) -> List[Transaction]:
        existing_user = await self._uow.user_repo.get_by_id(user_id)
        if existing_user is None:
            raise UserNotFoundError(user_id)
        return await self._uow.transaction_repo.get_user_transactions_list(
            user_id
        )
