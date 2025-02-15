from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AttachmentResourceRelationshipsTransactionData")


@_attrs_define
class AttachmentResourceRelationshipsTransactionData:
    """
    Attributes:
        type_ (str): The type of this resource: `transactions`
        id (str): The unique identifier of the resource within its type.
    """

    type_: str
    id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        type_ = d.pop("type")

        id = d.pop("id")

        attachment_resource_relationships_transaction_data = cls(
            type_=type_,
            id=id,
        )

        attachment_resource_relationships_transaction_data.additional_properties = d
        return attachment_resource_relationships_transaction_data

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
