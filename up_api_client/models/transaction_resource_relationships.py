from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.transaction_resource_relationships_account import (
        TransactionResourceRelationshipsAccount,
    )
    from ..models.transaction_resource_relationships_attachment import (
        TransactionResourceRelationshipsAttachment,
    )
    from ..models.transaction_resource_relationships_category import (
        TransactionResourceRelationshipsCategory,
    )
    from ..models.transaction_resource_relationships_parent_category import (
        TransactionResourceRelationshipsParentCategory,
    )
    from ..models.transaction_resource_relationships_tags import (
        TransactionResourceRelationshipsTags,
    )
    from ..models.transaction_resource_relationships_transfer_account import (
        TransactionResourceRelationshipsTransferAccount,
    )


T = TypeVar("T", bound="TransactionResourceRelationships")


@_attrs_define
class TransactionResourceRelationships:
    """
    Attributes:
        account (TransactionResourceRelationshipsAccount):
        transfer_account (TransactionResourceRelationshipsTransferAccount): If this transaction is a transfer between
            accounts, this relationship
            will contain the account the transaction went to/came from. The
            `amount` field can be used to determine the direction of the transfer.
        category (TransactionResourceRelationshipsCategory):
        parent_category (TransactionResourceRelationshipsParentCategory):
        tags (TransactionResourceRelationshipsTags):
        attachment (TransactionResourceRelationshipsAttachment):
    """

    account: "TransactionResourceRelationshipsAccount"
    transfer_account: "TransactionResourceRelationshipsTransferAccount"
    category: "TransactionResourceRelationshipsCategory"
    parent_category: "TransactionResourceRelationshipsParentCategory"
    tags: "TransactionResourceRelationshipsTags"
    attachment: "TransactionResourceRelationshipsAttachment"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account = self.account.to_dict()

        transfer_account = self.transfer_account.to_dict()

        category = self.category.to_dict()

        parent_category = self.parent_category.to_dict()

        tags = self.tags.to_dict()

        attachment = self.attachment.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account": account,
                "transferAccount": transfer_account,
                "category": category,
                "parentCategory": parent_category,
                "tags": tags,
                "attachment": attachment,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.transaction_resource_relationships_account import (
            TransactionResourceRelationshipsAccount,
        )
        from ..models.transaction_resource_relationships_attachment import (
            TransactionResourceRelationshipsAttachment,
        )
        from ..models.transaction_resource_relationships_category import (
            TransactionResourceRelationshipsCategory,
        )
        from ..models.transaction_resource_relationships_parent_category import (
            TransactionResourceRelationshipsParentCategory,
        )
        from ..models.transaction_resource_relationships_tags import (
            TransactionResourceRelationshipsTags,
        )
        from ..models.transaction_resource_relationships_transfer_account import (
            TransactionResourceRelationshipsTransferAccount,
        )

        d = src_dict.copy()
        account = TransactionResourceRelationshipsAccount.from_dict(d.pop("account"))

        transfer_account = TransactionResourceRelationshipsTransferAccount.from_dict(
            d.pop("transferAccount")
        )

        category = TransactionResourceRelationshipsCategory.from_dict(d.pop("category"))

        parent_category = TransactionResourceRelationshipsParentCategory.from_dict(
            d.pop("parentCategory")
        )

        tags = TransactionResourceRelationshipsTags.from_dict(d.pop("tags"))

        attachment = TransactionResourceRelationshipsAttachment.from_dict(
            d.pop("attachment")
        )

        transaction_resource_relationships = cls(
            account=account,
            transfer_account=transfer_account,
            category=category,
            parent_category=parent_category,
            tags=tags,
            attachment=attachment,
        )

        transaction_resource_relationships.additional_properties = d
        return transaction_resource_relationships

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
