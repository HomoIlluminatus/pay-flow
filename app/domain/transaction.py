from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID

from domain.base_entity import BaseEtity


@dataclass
class Transaction(BaseEtity):
    user_id: UUID
    account_id: UUID
    amount: Decimal
    