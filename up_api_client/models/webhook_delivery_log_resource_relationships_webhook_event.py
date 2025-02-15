from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.webhook_delivery_log_resource_relationships_webhook_event_data import (
        WebhookDeliveryLogResourceRelationshipsWebhookEventData,
    )


T = TypeVar("T", bound="WebhookDeliveryLogResourceRelationshipsWebhookEvent")


@_attrs_define
class WebhookDeliveryLogResourceRelationshipsWebhookEvent:
    """
    Attributes:
        data (WebhookDeliveryLogResourceRelationshipsWebhookEventData):
    """

    data: "WebhookDeliveryLogResourceRelationshipsWebhookEventData"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.webhook_delivery_log_resource_relationships_webhook_event_data import (
            WebhookDeliveryLogResourceRelationshipsWebhookEventData,
        )

        d = src_dict.copy()
        data = WebhookDeliveryLogResourceRelationshipsWebhookEventData.from_dict(
            d.pop("data")
        )

        webhook_delivery_log_resource_relationships_webhook_event = cls(
            data=data,
        )

        webhook_delivery_log_resource_relationships_webhook_event.additional_properties = d
        return webhook_delivery_log_resource_relationships_webhook_event

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
