from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tag_resource_relationships_transactions_links import (
        TagResourceRelationshipsTransactionsLinks,
    )


T = TypeVar("T", bound="TagResourceRelationshipsTransactions")


@_attrs_define
class TagResourceRelationshipsTransactions:
    """
    Attributes:
        links (Union[Unset, TagResourceRelationshipsTransactionsLinks]):
    """

    links: Union[Unset, "TagResourceRelationshipsTransactionsLinks"] = UNSET
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
        from ..models.tag_resource_relationships_transactions_links import (
            TagResourceRelationshipsTransactionsLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, TagResourceRelationshipsTransactionsLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = TagResourceRelationshipsTransactionsLinks.from_dict(_links)

        tag_resource_relationships_transactions = cls(
            links=links,
        )

        tag_resource_relationships_transactions.additional_properties = d
        return tag_resource_relationships_transactions

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
