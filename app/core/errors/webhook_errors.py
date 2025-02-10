from dataclasses import dataclass

from .base_error import BaseAppError


@dataclass
class WebHookError(BaseAppError):
    @property
    def message(self) -> str:
        return "Webhook error"
    

@dataclass
class SignatureError(WebHookError):
    @property
    def message(self):
        return "Invalid signagure"
    