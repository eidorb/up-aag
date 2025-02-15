from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.attachment_resource_relationships_transaction import (
        AttachmentResourceRelationshipsTransaction,
    )


T = TypeVar("T", bound="AttachmentResourceRelationships")


@_attrs_define
class AttachmentResourceRelationships:
    """
    Attributes:
        transaction (AttachmentResourceRelationshipsTransaction):
    """

    transaction: "AttachmentResourceRelationshipsTransaction"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        transaction = self.transaction.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "transaction": transaction,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.attachment_resource_relationships_transaction import (
            AttachmentResourceRelationshipsTransaction,
        )

        d = src_dict.copy()
        transaction = AttachmentResourceRelationshipsTransaction.from_dict(
            d.pop("transaction")
        )

        attachment_resource_relationships = cls(
            transaction=transaction,
        )

        attachment_resource_relationships.additional_properties = d
        return attachment_resource_relationships

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
