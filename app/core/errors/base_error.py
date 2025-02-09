from dataclasses import dataclass


@dataclass
class BaseAppError(Exception):
    @property
    def message(self):
        return "Base aplication error"
    