from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.webhook_input_resource_attributes import (
        WebhookInputResourceAttributes,
    )


T = TypeVar("T", bound="WebhookInputResource")


@_attrs_define
class WebhookInputResource:
    """Represents a webhook specified as request input.

    Attributes:
        attributes (WebhookInputResourceAttributes):
    """

    attributes: "WebhookInputResourceAttributes"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attributes": attributes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.webhook_input_resource_attributes import (
            WebhookInputResourceAttributes,
        )

        d = src_dict.copy()
        attributes = WebhookInputResourceAttributes.from_dict(d.pop("attributes"))

        webhook_input_resource = cls(
            attributes=attributes,
        )

        webhook_input_resource.additional_properties = d
        return webhook_input_resource

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
