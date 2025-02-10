from typing import List
from uuid import UUID

from core.errors.account_errors import AccountNotFoundError
from core.errors.user_errors import UserNotFoundError
from domain.account import Account
from repositories.base_uow import UnitOfWork


class AccountService:
    def __init__(self, uow: UnitOfWork) -> None:
        self._uow = uow
        
    async def get_account_or_raise(self, account_id: UUID) -> Account:
        account = await self._uow.account_repo.get_by_id(account_id)
        if account is None:
            raise AccountNotFoundError(account_id)
        return account
        
    async def get_user_accounts_list(self, user_id: UUID) -> List[Account]:
        existing_user = await self._uow.user_repo.get_by_id(user_id)
        if existing_user is None:
            raise UserNotFoundError(user_id)
        return await self._uow.account_repo.get_user_accounts_list(self)
    
    async def update_account(self, account: Account) -> Account:
        async with self._uow:
            await self._uow.account_repo.update(account)
            await self._uow.commit()
            return account
        
    async def delete_account(self, account_id: UUID) -> None:
        async with self._uow:
            await self._uow.account_repo.delete(account_id)
            await self._uow.commit()
            