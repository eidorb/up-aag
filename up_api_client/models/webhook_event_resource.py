from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.webhook_event_resource_attributes import (
        WebhookEventResourceAttributes,
    )
    from ..models.webhook_event_resource_relationships import (
        WebhookEventResourceRelationships,
    )


T = TypeVar("T", bound="WebhookEventResource")


@_attrs_define
class WebhookEventResource:
    """Provides the event data used in asynchronous webhook event callbacks to
    subscribed endpoints. Webhooks events have defined `eventType`s and may
    optionally relate to other resources within the Up API.

        Attributes:
            type_ (str): The type of this resource: `webhook-events`
            id (str): The unique identifier for this event. This will remain constant across
                delivery retries.
            attributes (WebhookEventResourceAttributes):
            relationships (WebhookEventResourceRelationships):
    """

    type_: str
    id: str
    attributes: "WebhookEventResourceAttributes"
    relationships: "WebhookEventResourceRelationships"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        id = self.id

        attributes = self.attributes.to_dict()

        relationships = self.relationships.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "id": id,
                "attributes": attributes,
                "relationships": relationships,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.webhook_event_resource_attributes import (
            WebhookEventResourceAttributes,
        )
        from ..models.webhook_event_resource_relationships import (
            WebhookEventResourceRelationships,
        )

        d = src_dict.copy()
        type_ = d.pop("type")

        id = d.pop("id")

        attributes = WebhookEventResourceAttributes.from_dict(d.pop("attributes"))

        relationships = WebhookEventResourceRelationships.from_dict(
            d.pop("relationships")
        )

        webhook_event_resource = cls(
            type_=type_,
            id=id,
            attributes=attributes,
            relationships=relationships,
        )

        webhook_event_resource.additional_properties = d
        return webhook_event_resource

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
