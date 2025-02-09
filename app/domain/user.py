from dataclasses import dataclass, field

from . base_entity import BaseEtity


@dataclass
class User(BaseEtity):
    email: str
    full_name: str
    hashed_password: str
    is_admin: bool = field(default=False)
    