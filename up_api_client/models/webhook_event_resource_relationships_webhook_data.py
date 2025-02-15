from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WebhookEventResourceRelationshipsWebhookData")


@_attrs_define
class WebhookEventResourceRelationshipsWebhookData:
    """
    Attributes:
        type_ (str): The type of this resource: `webhooks`
        id (str): The unique identifier of the resource within its type.
    """

    type_: str
    id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        type_ = d.pop("type")

        id = d.pop("id")

        webhook_event_resource_relationships_webhook_data = cls(
            type_=type_,
            id=id,
        )

        webhook_event_resource_relationships_webhook_data.additional_properties = d
        return webhook_event_resource_relationships_webhook_data

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
