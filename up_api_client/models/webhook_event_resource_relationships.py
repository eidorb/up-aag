from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_event_resource_relationships_transaction import (
        WebhookEventResourceRelationshipsTransaction,
    )
    from ..models.webhook_event_resource_relationships_webhook import (
        WebhookEventResourceRelationshipsWebhook,
    )


T = TypeVar("T", bound="WebhookEventResourceRelationships")


@_attrs_define
class WebhookEventResourceRelationships:
    """
    Attributes:
        webhook (WebhookEventResourceRelationshipsWebhook):
        transaction (Union[Unset, WebhookEventResourceRelationshipsTransaction]):
    """

    webhook: "WebhookEventResourceRelationshipsWebhook"
    transaction: Union[Unset, "WebhookEventResourceRelationshipsTransaction"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        webhook = self.webhook.to_dict()

        transaction: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.transaction, Unset):
            transaction = self.transaction.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "webhook": webhook,
            }
        )
        if transaction is not UNSET:
            field_dict["transaction"] = transaction

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.webhook_event_resource_relationships_transaction import (
            WebhookEventResourceRelationshipsTransaction,
        )
        from ..models.webhook_event_resource_relationships_webhook import (
            WebhookEventResourceRelationshipsWebhook,
        )

        d = src_dict.copy()
        webhook = WebhookEventResourceRelationshipsWebhook.from_dict(d.pop("webhook"))

        _transaction = d.pop("transaction", UNSET)
        transaction: Union[Unset, WebhookEventResourceRelationshipsTransaction]
        if isinstance(_transaction, Unset):
            transaction = UNSET
        else:
            transaction = WebhookEventResourceRelationshipsTransaction.from_dict(
                _transaction
            )

        webhook_event_resource_relationships = cls(
            webhook=webhook,
            transaction=transaction,
        )

        webhook_event_resource_relationships.additional_properties = d
        return webhook_event_resource_relationships

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
