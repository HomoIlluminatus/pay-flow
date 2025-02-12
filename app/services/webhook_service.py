from decimal import Decimal
from typing import Optional
from uuid import UUID

from core.errors.transaction_errors import TransactionExistError
from core.errors.user_errors import UserNotFoundError
from core.errors.webhook_errors import SignatureError
from domain.account import Account
from domain.transaction import Transaction
from repositories.base_uow import UnitOfWork


class WebHookService:
    def __init__(self, uow: UnitOfWork, secret_key) -> None:
        self._uow = uow
        self._secret_key = secret_key
        
    async def _is_exist_user(self, user_id: UUID) -> bool:
        user = await self._uow.user_repo.get_by_id(user_id)
        return user is not None

    @staticmethod
    def _get_signature(
        account_id: UUID,
        amount: Decimal,
        transaction_id: UUID,
        user_id: UUID,
        secret_key: str
    ) -> str:
        return f"{account_id}{amount}{transaction_id}{user_id}{secret_key}"
    
    async def process_webhook(
        self,
        account_id: UUID,
        amount: Decimal,
        transaction_id: UUID,
        user_id: UUID,
        signature: str
    ) -> Optional[Transaction]:
        if signature != self._get_signature(account_id, amount,
                                            transaction_id, user_id,
                                            self._secret_key):
                raise SignatureError
            
        if not await self._is_exist_user(user_id):
            raise UserNotFoundError(user_id)
        
        if await self._uow.transaction_repo.get_by_id(transaction_id):
                raise TransactionExistError(transaction_id)
            
        async with self._uow:
            account = await self._uow.account_repo.get_by_id(account_id)
            
            if account is None:
                account =  Account(user_id=user_id)
                account.deposit(amount)
                await self._uow.account_repo.add(account)
            else:
                account.deposit(amount)
                await self._uow.account_repo.update(account)
            
            transaction = Transaction(transaction_id, amount)
            await self._uow.transaction_repo.add(transaction)
            
            return transaction            
            