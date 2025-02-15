from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.money_object import MoneyObject


T = TypeVar("T", bound="CashbackObject")


@_attrs_define
class CashbackObject:
    """Provides information about an instant reimbursement in the form of
    cashback.

        Attributes:
            description (str): A brief description of why this cashback was paid.
            amount (MoneyObject): Provides information about a value of money.
    """

    description: str
    amount: "MoneyObject"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        amount = self.amount.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "amount": amount,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.money_object import MoneyObject

        d = src_dict.copy()
        description = d.pop("description")

        amount = MoneyObject.from_dict(d.pop("amount"))

        cashback_object = cls(
            description=description,
            amount=amount,
        )

        cashback_object.additional_properties = d
        return cashback_object

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
