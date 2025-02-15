from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ListWebhookDeliveryLogsResponseLinks")


@_attrs_define
class ListWebhookDeliveryLogsResponseLinks:
    """
    Attributes:
        prev (Union[None, str]): The link to the previous page in the results. If this value is `null`
            there is no previous page.
        next_ (Union[None, str]): The link to the next page in the results. If this value is `null`
            there is no next page.
    """

    prev: Union[None, str]
    next_: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        prev: Union[None, str]
        prev = self.prev

        next_: Union[None, str]
        next_ = self.next_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "prev": prev,
                "next": next_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_prev(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        prev = _parse_prev(d.pop("prev"))

        def _parse_next_(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        next_ = _parse_next_(d.pop("next"))

        list_webhook_delivery_logs_response_links = cls(
            prev=prev,
            next_=next_,
        )

        list_webhook_delivery_logs_response_links.additional_properties = d
        return list_webhook_delivery_logs_response_links

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
