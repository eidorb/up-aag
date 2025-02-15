from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.money_object import MoneyObject


T = TypeVar("T", bound="HoldInfoObject")


@_attrs_define
class HoldInfoObject:
    """Provides information about the amount at which a transaction was in the
    `HELD` status.

        Attributes:
            amount (MoneyObject): Provides information about a value of money.
            foreign_amount (Union['MoneyObject', None]): The foreign currency amount of this transaction while in the `HELD`
                status. This field will be `null` for domestic transactions. The amount
                was converted to the AUD amount reflected in the `amount` field.
    """

    amount: "MoneyObject"
    foreign_amount: Union["MoneyObject", None]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.money_object import MoneyObject

        amount = self.amount.to_dict()

        foreign_amount: Union[None, dict[str, Any]]
        if isinstance(self.foreign_amount, MoneyObject):
            foreign_amount = self.foreign_amount.to_dict()
        else:
            foreign_amount = self.foreign_amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount": amount,
                "foreignAmount": foreign_amount,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.money_object import MoneyObject

        d = src_dict.copy()
        amount = MoneyObject.from_dict(d.pop("amount"))

        def _parse_foreign_amount(data: object) -> Union["MoneyObject", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                foreign_amount_type_1 = MoneyObject.from_dict(data)

                return foreign_amount_type_1
            except:  # noqa: E722
                pass
            return cast(Union["MoneyObject", None], data)

        foreign_amount = _parse_foreign_amount(d.pop("foreignAmount"))

        hold_info_object = cls(
            amount=amount,
            foreign_amount=foreign_amount,
        )

        hold_info_object.additional_properties = d
        return hold_info_object

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
