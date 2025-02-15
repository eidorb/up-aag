from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_webhooks_response_links import ListWebhooksResponseLinks
    from ..models.webhook_resource import WebhookResource


T = TypeVar("T", bound="ListWebhooksResponse")


@_attrs_define
class ListWebhooksResponse:
    """Successful response to get all webhooks. This returns a paginated list of
    webhooks, which can be scrolled by following the `prev` and `next` links
    if present.

        Attributes:
            data (list['WebhookResource']): The list of webhooks returned in this response.
            links (ListWebhooksResponseLinks):
    """

    data: list["WebhookResource"]
    links: "ListWebhooksResponseLinks"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        links = self.links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "links": links,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.list_webhooks_response_links import ListWebhooksResponseLinks
        from ..models.webhook_resource import WebhookResource

        d = src_dict.copy()
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = WebhookResource.from_dict(data_item_data)

            data.append(data_item)

        links = ListWebhooksResponseLinks.from_dict(d.pop("links"))

        list_webhooks_response = cls(
            data=data,
            links=links,
        )

        list_webhooks_response.additional_properties = d
        return list_webhooks_response

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
