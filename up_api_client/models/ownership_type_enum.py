from enum import Enum


class OwnershipTypeEnum(str, Enum):
    INDIVIDUAL = "INDIVIDUAL"
    JOINT = "JOINT"

    def __str__(self) -> str:
        return str(self.value)
