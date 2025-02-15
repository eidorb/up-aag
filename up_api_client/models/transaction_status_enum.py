from enum import Enum


class TransactionStatusEnum(str, Enum):
    HELD = "HELD"
    SETTLED = "SETTLED"

    def __str__(self) -> str:
        return str(self.value)
