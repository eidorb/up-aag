from enum import Enum


class WebhookEventTypeEnum(str, Enum):
    PING = "PING"
    TRANSACTION_CREATED = "TRANSACTION_CREATED"
    TRANSACTION_DELETED = "TRANSACTION_DELETED"
    TRANSACTION_SETTLED = "TRANSACTION_SETTLED"

    def __str__(self) -> str:
        return str(self.value)
