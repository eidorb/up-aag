from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MoneyObject")


@_attrs_define
class MoneyObject:
    """Provides information about a value of money.

    Attributes:
        currency_code (str): The ISO 4217 currency code.
        value (str): The amount of money, formatted as a string in the relevant currency.
            For example, for an Australian dollar value of $10.56, this field will
            be `"10.56"`. The currency symbol is not included in the string.
        value_in_base_units (int): The amount of money in the smallest denomination for the currency, as a
            64-bit integer.  For example, for an Australian dollar value of $10.56,
            this field will be `1056`.
    """

    currency_code: str
    value: str
    value_in_base_units: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency_code = self.currency_code

        value = self.value

        value_in_base_units = self.value_in_base_units

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currencyCode": currency_code,
                "value": value,
                "valueInBaseUnits": value_in_base_units,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        currency_code = d.pop("currencyCode")

        value = d.pop("value")

        value_in_base_units = d.pop("valueInBaseUnits")

        money_object = cls(
            currency_code=currency_code,
            value=value,
            value_in_base_units=value_in_base_units,
        )

        money_object.additional_properties = d
        return money_object

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
