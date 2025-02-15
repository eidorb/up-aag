from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.tag_resource_relationships import TagResourceRelationships


T = TypeVar("T", bound="TagResource")


@_attrs_define
class TagResource:
    """Provides information about a tag.

    Attributes:
        type_ (str): The type of this resource: `tags`
        id (str): The label of the tag, which also acts as the tag’s unique identifier.
        relationships (TagResourceRelationships):
    """

    type_: str
    id: str
    relationships: "TagResourceRelationships"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        id = self.id

        relationships = self.relationships.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "id": id,
                "relationships": relationships,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.tag_resource_relationships import TagResourceRelationships

        d = src_dict.copy()
        type_ = d.pop("type")

        id = d.pop("id")

        relationships = TagResourceRelationships.from_dict(d.pop("relationships"))

        tag_resource = cls(
            type_=type_,
            id=id,
            relationships=relationships,
        )

        tag_resource.additional_properties = d
        return tag_resource

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
