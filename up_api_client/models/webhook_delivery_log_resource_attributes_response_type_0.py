from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WebhookDeliveryLogResourceAttributesResponseType0")


@_attrs_define
class WebhookDeliveryLogResourceAttributesResponseType0:
    """Information about the response that was received from the webhook URL.

    Attributes:
        status_code (int): The HTTP status code received in the response.
        body (str): The payload that was received in the response body.
    """

    status_code: int
    body: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status_code = self.status_code

        body = self.body

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "statusCode": status_code,
                "body": body,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        status_code = d.pop("statusCode")

        body = d.pop("body")

        webhook_delivery_log_resource_attributes_response_type_0 = cls(
            status_code=status_code,
            body=body,
        )

        webhook_delivery_log_resource_attributes_response_type_0.additional_properties = d
        return webhook_delivery_log_resource_attributes_response_type_0

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
