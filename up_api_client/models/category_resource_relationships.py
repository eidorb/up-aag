from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.category_resource_relationships_children import (
        CategoryResourceRelationshipsChildren,
    )
    from ..models.category_resource_relationships_parent import (
        CategoryResourceRelationshipsParent,
    )


T = TypeVar("T", bound="CategoryResourceRelationships")


@_attrs_define
class CategoryResourceRelationships:
    """
    Attributes:
        parent (CategoryResourceRelationshipsParent):
        children (CategoryResourceRelationshipsChildren):
    """

    parent: "CategoryResourceRelationshipsParent"
    children: "CategoryResourceRelationshipsChildren"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parent = self.parent.to_dict()

        children = self.children.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parent": parent,
                "children": children,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.category_resource_relationships_children import (
            CategoryResourceRelationshipsChildren,
        )
        from ..models.category_resource_relationships_parent import (
            CategoryResourceRelationshipsParent,
        )

        d = src_dict.copy()
        parent = CategoryResourceRelationshipsParent.from_dict(d.pop("parent"))

        children = CategoryResourceRelationshipsChildren.from_dict(d.pop("children"))

        category_resource_relationships = cls(
            parent=parent,
            children=children,
        )

        category_resource_relationships.additional_properties = d
        return category_resource_relationships

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
