from abc import ABC
from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID, uuid4


@dataclass
class BaseEtity(ABC):
    id: UUID = field(default_factory=uuid4, kw_only=True)
    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc),
        kw_only=True
    )
    updated_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc),
        kw_only=True
    )
    
    def updatetimestemp(self) -> None:
        self.updated_at = datetime.now(timezone.utc)
        