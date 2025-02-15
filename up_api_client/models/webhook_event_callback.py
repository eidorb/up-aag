from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.webhook_event_resource import WebhookEventResource


T = TypeVar("T", bound="WebhookEventCallback")


@_attrs_define
class WebhookEventCallback:
    """Asynchronous callback request used for webhook event delivery.

    Attributes:
        data (WebhookEventResource): Provides the event data used in asynchronous webhook event callbacks to
            subscribed endpoints. Webhooks events have defined `eventType`s and may
            optionally relate to other resources within the Up API.
    """

    data: "WebhookEventResource"
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
        from ..models.webhook_event_resource import WebhookEventResource

        d = src_dict.copy()
        data = WebhookEventResource.from_dict(d.pop("data"))

        webhook_event_callback = cls(
            data=data,
        )

        webhook_event_callback.additional_properties = d
        return webhook_event_callback

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
