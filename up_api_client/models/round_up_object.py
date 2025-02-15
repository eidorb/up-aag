from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.money_object import MoneyObject


T = TypeVar("T", bound="RoundUpObject")


@_attrs_define
class RoundUpObject:
    """Provides information about how a Round Up was applied, such as whether or
    not a boost was included in the Round Up.

        Attributes:
            amount (MoneyObject): Provides information about a value of money.
            boost_portion (Union['MoneyObject', None]): The portion of the Round Up `amount` owing to boosted Round Ups,
                represented as a negative value. If no boost was added to the Round Up
                this field will be `null`.
    """

    amount: "MoneyObject"
    boost_portion: Union["MoneyObject", None]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.money_object import MoneyObject

        amount = self.amount.to_dict()

        boost_portion: Union[None, dict[str, Any]]
        if isinstance(self.boost_portion, MoneyObject):
            boost_portion = self.boost_portion.to_dict()
        else:
            boost_portion = self.boost_portion

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount": amount,
                "boostPortion": boost_portion,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.money_object import MoneyObject

        d = src_dict.copy()
        amount = MoneyObject.from_dict(d.pop("amount"))

        def _parse_boost_portion(data: object) -> Union["MoneyObject", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                boost_portion_type_1 = MoneyObject.from_dict(data)

                return boost_portion_type_1
            except:  # noqa: E722
                pass
            return cast(Union["MoneyObject", None], data)

        boost_portion = _parse_boost_portion(d.pop("boostPortion"))

        round_up_object = cls(
            amount=amount,
            boost_portion=boost_portion,
        )

        round_up_object.additional_properties = d
        return round_up_object

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
