from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attachment_resource_relationships_transaction_data import (
        AttachmentResourceRelationshipsTransactionData,
    )
    from ..models.attachment_resource_relationships_transaction_links import (
        AttachmentResourceRelationshipsTransactionLinks,
    )


T = TypeVar("T", bound="AttachmentResourceRelationshipsTransaction")


@_attrs_define
class AttachmentResourceRelationshipsTransaction:
    """
    Attributes:
        data (AttachmentResourceRelationshipsTransactionData):
        links (Union[Unset, AttachmentResourceRelationshipsTransactionLinks]):
    """

    data: "AttachmentResourceRelationshipsTransactionData"
    links: Union[Unset, "AttachmentResourceRelationshipsTransactionLinks"] = UNSET
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
        from ..models.attachment_resource_relationships_transaction_data import (
            AttachmentResourceRelationshipsTransactionData,
        )
        from ..models.attachment_resource_relationships_transaction_links import (
            AttachmentResourceRelationshipsTransactionLinks,
        )

        d = src_dict.copy()
        data = AttachmentResourceRelationshipsTransactionData.from_dict(d.pop("data"))

        _links = d.pop("links", UNSET)
        links: Union[Unset, AttachmentResourceRelationshipsTransactionLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = AttachmentResourceRelationshipsTransactionLinks.from_dict(_links)

        attachment_resource_relationships_transaction = cls(
            data=data,
            links=links,
        )

        attachment_resource_relationships_transaction.additional_properties = d
        return attachment_resource_relationships_transaction

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
