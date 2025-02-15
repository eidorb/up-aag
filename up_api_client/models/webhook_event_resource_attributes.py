import datetime
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.webhook_event_type_enum import WebhookEventTypeEnum

T = TypeVar("T", bound="WebhookEventResourceAttributes")


@_attrs_define
class WebhookEventResourceAttributes:
    """
    Attributes:
        event_type (WebhookEventTypeEnum): Specifies the type of a webhook event. This can be used to determine what
            action to take in response to the event, such as which relationships to
            expect.
        created_at (datetime.datetime): The date-time at which this event was generated.
    """

    event_type: WebhookEventTypeEnum
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_type = self.event_type.value

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eventType": event_type,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        event_type = WebhookEventTypeEnum(d.pop("eventType"))

        created_at = isoparse(d.pop("createdAt"))

        webhook_event_resource_attributes = cls(
            event_type=event_type,
            created_at=created_at,
        )

        webhook_event_resource_attributes.additional_properties = d
        return webhook_event_resource_attributes

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
