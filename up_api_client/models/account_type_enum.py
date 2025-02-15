from enum import Enum


class AccountTypeEnum(str, Enum):
    HOME_LOAN = "HOME_LOAN"
    SAVER = "SAVER"
    TRANSACTIONAL = "TRANSACTIONAL"

    def __str__(self) -> str:
        return str(self.value)
