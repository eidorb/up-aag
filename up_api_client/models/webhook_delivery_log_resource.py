from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.webhook_delivery_log_resource_attributes import (
        WebhookDeliveryLogResourceAttributes,
    )
    from ..models.webhook_delivery_log_resource_relationships import (
        WebhookDeliveryLogResourceRelationships,
    )


T = TypeVar("T", bound="WebhookDeliveryLogResource")


@_attrs_define
class WebhookDeliveryLogResource:
    """Provides historical webhook event delivery information for analysis and
    debugging purposes.

        Attributes:
            type_ (str): The type of this resource: `webhook-delivery-logs`
            id (str): The unique identifier for this log entry.
            attributes (WebhookDeliveryLogResourceAttributes):
            relationships (WebhookDeliveryLogResourceRelationships):
    """

    type_: str
    id: str
    attributes: "WebhookDeliveryLogResourceAttributes"
    relationships: "WebhookDeliveryLogResourceRelationships"
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
        from ..models.webhook_delivery_log_resource_attributes import (
            WebhookDeliveryLogResourceAttributes,
        )
        from ..models.webhook_delivery_log_resource_relationships import (
            WebhookDeliveryLogResourceRelationships,
        )

        d = src_dict.copy()
        type_ = d.pop("type")

        id = d.pop("id")

        attributes = WebhookDeliveryLogResourceAttributes.from_dict(d.pop("attributes"))

        relationships = WebhookDeliveryLogResourceRelationships.from_dict(
            d.pop("relationships")
        )

        webhook_delivery_log_resource = cls(
            type_=type_,
            id=id,
            attributes=attributes,
            relationships=relationships,
        )

        webhook_delivery_log_resource.additional_properties = d
        return webhook_delivery_log_resource

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
