from enum import Enum


class WebhookDeliveryStatusEnum(str, Enum):
    BAD_RESPONSE_CODE = "BAD_RESPONSE_CODE"
    DELIVERED = "DELIVERED"
    UNDELIVERABLE = "UNDELIVERABLE"

    def __str__(self) -> str:
        return str(self.value)
