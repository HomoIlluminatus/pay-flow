from dataclasses import dataclass
from uuid import UUID

from errors.base_error import BaseAppError


@dataclass
class UserError(BaseAppError):
    @property
    def message(self) -> str:
        return "User error"


@dataclass
class UserNotFoundError(UserError):
    user_id: UUID

    @property
    def message(self) -> str:
        return f"User not found: ID {self.user_id}"


@dataclass
class UserExistError(UserError):
    email: str

    @property
    def message(self) -> str:
        return f"User with email {self.email} already exists"
