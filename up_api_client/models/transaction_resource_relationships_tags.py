from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transaction_resource_relationships_tags_data_item import (
        TransactionResourceRelationshipsTagsDataItem,
    )
    from ..models.transaction_resource_relationships_tags_links import (
        TransactionResourceRelationshipsTagsLinks,
    )


T = TypeVar("T", bound="TransactionResourceRelationshipsTags")


@_attrs_define
class TransactionResourceRelationshipsTags:
    """
    Attributes:
        data (list['TransactionResourceRelationshipsTagsDataItem']):
        links (Union[Unset, TransactionResourceRelationshipsTagsLinks]):
    """

    data: list["TransactionResourceRelationshipsTagsDataItem"]
    links: Union[Unset, "TransactionResourceRelationshipsTagsLinks"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

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
        from ..models.transaction_resource_relationships_tags_data_item import (
            TransactionResourceRelationshipsTagsDataItem,
        )
        from ..models.transaction_resource_relationships_tags_links import (
            TransactionResourceRelationshipsTagsLinks,
        )

        d = src_dict.copy()
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = TransactionResourceRelationshipsTagsDataItem.from_dict(
                data_item_data
            )

            data.append(data_item)

        _links = d.pop("links", UNSET)
        links: Union[Unset, TransactionResourceRelationshipsTagsLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = TransactionResourceRelationshipsTagsLinks.from_dict(_links)

        transaction_resource_relationships_tags = cls(
            data=data,
            links=links,
        )

        transaction_resource_relationships_tags.additional_properties = d
        return transaction_resource_relationships_tags

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
