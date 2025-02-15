from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_resource_relationships_logs_links import (
        WebhookResourceRelationshipsLogsLinks,
    )


T = TypeVar("T", bound="WebhookResourceRelationshipsLogs")


@_attrs_define
class WebhookResourceRelationshipsLogs:
    """
    Attributes:
        links (Union[Unset, WebhookResourceRelationshipsLogsLinks]):
    """

    links: Union[Unset, "WebhookResourceRelationshipsLogsLinks"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.webhook_resource_relationships_logs_links import (
            WebhookResourceRelationshipsLogsLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, WebhookResourceRelationshipsLogsLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = WebhookResourceRelationshipsLogsLinks.from_dict(_links)

        webhook_resource_relationships_logs = cls(
            links=links,
        )

        webhook_resource_relationships_logs.additional_properties = d
        return webhook_resource_relationships_logs

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
