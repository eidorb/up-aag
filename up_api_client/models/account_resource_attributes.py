import datetime
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.account_type_enum import AccountTypeEnum
from ..models.ownership_type_enum import OwnershipTypeEnum

if TYPE_CHECKING:
    from ..models.money_object import MoneyObject


T = TypeVar("T", bound="AccountResourceAttributes")


@_attrs_define
class AccountResourceAttributes:
    """
    Attributes:
        display_name (str): The name associated with the account in the Up application.
        account_type (AccountTypeEnum): Specifies the type of bank account. Currently returned values are
            `SAVER`, `TRANSACTIONAL` and `HOME_LOAN`.
        ownership_type (OwnershipTypeEnum): Specifies the structure under which a bank account is owned. Currently
            returned values are `INDIVIDUAL` and `JOINT`.
        balance (MoneyObject): Provides information about a value of money.
        created_at (datetime.datetime): The date-time at which this account was first opened.
    """

    display_name: str
    account_type: AccountTypeEnum
    ownership_type: OwnershipTypeEnum
    balance: "MoneyObject"
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        account_type = self.account_type.value

        ownership_type = self.ownership_type.value

        balance = self.balance.to_dict()

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "displayName": display_name,
                "accountType": account_type,
                "ownershipType": ownership_type,
                "balance": balance,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.money_object import MoneyObject

        d = src_dict.copy()
        display_name = d.pop("displayName")

        account_type = AccountTypeEnum(d.pop("accountType"))

        ownership_type = OwnershipTypeEnum(d.pop("ownershipType"))

        balance = MoneyObject.from_dict(d.pop("balance"))

        created_at = isoparse(d.pop("createdAt"))

        account_resource_attributes = cls(
            display_name=display_name,
            account_type=account_type,
            ownership_type=ownership_type,
            balance=balance,
            created_at=created_at,
        )

        account_resource_attributes.additional_properties = d
        return account_resource_attributes

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
