from enum import Enum


class CardPurchaseMethodEnum(str, Enum):
    BAR_CODE = "BAR_CODE"
    CARD_DETAILS = "CARD_DETAILS"
    CARD_ON_FILE = "CARD_ON_FILE"
    CARD_PIN = "CARD_PIN"
    CONTACTLESS = "CONTACTLESS"
    ECOMMERCE = "ECOMMERCE"
    MAGNETIC_STRIPE = "MAGNETIC_STRIPE"
    OCR = "OCR"

    def __str__(self) -> str:
        return str(self.value)
