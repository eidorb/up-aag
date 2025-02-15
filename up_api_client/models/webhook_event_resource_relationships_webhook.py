from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_event_resource_relationships_webhook_data import (
        WebhookEventResourceRelationshipsWebhookData,
    )
    from ..models.webhook_event_resource_relationships_webhook_links import (
        WebhookEventResourceRelationshipsWebhookLinks,
    )


T = TypeVar("T", bound="WebhookEventResourceRelationshipsWebhook")


@_attrs_define
class WebhookEventResourceRelationshipsWebhook:
    """
    Attributes:
        data (WebhookEventResourceRelationshipsWebhookData):
        links (Union[Unset, WebhookEventResourceRelationshipsWebhookLinks]):
    """

    data: "WebhookEventResourceRelationshipsWebhookData"
    links: Union[Unset, "WebhookEventResourceRelationshipsWebhookLinks"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.webhook_event_resource_relationships_webhook_data import (
            WebhookEventResourceRelationshipsWebhookData,
        )
        from ..models.webhook_event_resource_relationships_webhook_links import (
            WebhookEventResourceRelationshipsWebhookLinks,
        )

        d = src_dict.copy()
        data = WebhookEventResourceRelationshipsWebhookData.from_dict(d.pop("data"))

        _links = d.pop("links", UNSET)
        links: Union[Unset, WebhookEventResourceRelationshipsWebhookLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = WebhookEventResourceRelationshipsWebhookLinks.from_dict(_links)

        webhook_event_resource_relationships_webhook = cls(
            data=data,
            links=links,
        )

        webhook_event_resource_relationships_webhook.additional_properties = d
        return webhook_event_resource_relationships_webhook

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
