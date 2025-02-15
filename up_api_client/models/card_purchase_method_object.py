from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.card_purchase_method_enum import CardPurchaseMethodEnum

T = TypeVar("T", bound="CardPurchaseMethodObject")


@_attrs_define
class CardPurchaseMethodObject:
    """Provides information about the card used for a transaction.

    Attributes:
        method (CardPurchaseMethodEnum): Specifies the type of card charge.
        card_number_suffix (Union[None, str]): The last four digits of the card used for the purchase, if applicable.
    """

    method: CardPurchaseMethodEnum
    card_number_suffix: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method = self.method.value

        card_number_suffix: Union[None, str]
        card_number_suffix = self.card_number_suffix

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method": method,
                "cardNumberSuffix": card_number_suffix,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        method = CardPurchaseMethodEnum(d.pop("method"))

        def _parse_card_number_suffix(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        card_number_suffix = _parse_card_number_suffix(d.pop("cardNumberSuffix"))

        card_purchase_method_object = cls(
            method=method,
            card_number_suffix=card_number_suffix,
        )

        card_purchase_method_object.additional_properties = d
        return card_purchase_method_object

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
