from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.webhook_resource_relationships_logs import (
        WebhookResourceRelationshipsLogs,
    )


T = TypeVar("T", bound="WebhookResourceRelationships")


@_attrs_define
class WebhookResourceRelationships:
    """
    Attributes:
        logs (WebhookResourceRelationshipsLogs):
    """

    logs: "WebhookResourceRelationshipsLogs"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        logs = self.logs.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "logs": logs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.webhook_resource_relationships_logs import (
            WebhookResourceRelationshipsLogs,
        )

        d = src_dict.copy()
        logs = WebhookResourceRelationshipsLogs.from_dict(d.pop("logs"))

        webhook_resource_relationships = cls(
            logs=logs,
        )

        webhook_resource_relationships.additional_properties = d
        return webhook_resource_relationships

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
