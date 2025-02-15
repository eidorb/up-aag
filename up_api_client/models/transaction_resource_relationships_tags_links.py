from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TransactionResourceRelationshipsTagsLinks")


@_attrs_define
class TransactionResourceRelationshipsTagsLinks:
    """
    Attributes:
        self_ (str): The link to retrieve or modify linkage between this resources and the
            related resource(s) in this relationship.
    """

    self_: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_ = self.self_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "self": self_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        self_ = d.pop("self")

        transaction_resource_relationships_tags_links = cls(
            self_=self_,
        )

        transaction_resource_relationships_tags_links.additional_properties = d
        return transaction_resource_relationships_tags_links

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
