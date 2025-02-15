from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TagInputResourceIdentifier")


@_attrs_define
class TagInputResourceIdentifier:
    """Uniquely identifies a single tag in the API.

    Attributes:
        type_ (str): The type of this resource: `tags`
        id (str): The label of the tag, which also acts as the tag’s unique identifier.
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

        tag_input_resource_identifier = cls(
            type_=type_,
            id=id,
        )

        tag_input_resource_identifier.additional_properties = d
        return tag_input_resource_identifier

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
