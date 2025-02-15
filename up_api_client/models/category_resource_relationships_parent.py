from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.category_resource_relationships_parent_data_type_0 import (
        CategoryResourceRelationshipsParentDataType0,
    )
    from ..models.category_resource_relationships_parent_links import (
        CategoryResourceRelationshipsParentLinks,
    )


T = TypeVar("T", bound="CategoryResourceRelationshipsParent")


@_attrs_define
class CategoryResourceRelationshipsParent:
    """
    Attributes:
        data (Union['CategoryResourceRelationshipsParentDataType0', None]):
        links (Union[Unset, CategoryResourceRelationshipsParentLinks]):
    """

    data: Union["CategoryResourceRelationshipsParentDataType0", None]
    links: Union[Unset, "CategoryResourceRelationshipsParentLinks"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.category_resource_relationships_parent_data_type_0 import (
            CategoryResourceRelationshipsParentDataType0,
        )

        data: Union[None, dict[str, Any]]
        if isinstance(self.data, CategoryResourceRelationshipsParentDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

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
        from ..models.category_resource_relationships_parent_data_type_0 import (
            CategoryResourceRelationshipsParentDataType0,
        )
        from ..models.category_resource_relationships_parent_links import (
            CategoryResourceRelationshipsParentLinks,
        )

        d = src_dict.copy()

        def _parse_data(
            data: object,
        ) -> Union["CategoryResourceRelationshipsParentDataType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = CategoryResourceRelationshipsParentDataType0.from_dict(
                    data
                )

                return data_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union["CategoryResourceRelationshipsParentDataType0", None], data
            )

        data = _parse_data(d.pop("data"))

        _links = d.pop("links", UNSET)
        links: Union[Unset, CategoryResourceRelationshipsParentLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = CategoryResourceRelationshipsParentLinks.from_dict(_links)

        category_resource_relationships_parent = cls(
            data=data,
            links=links,
        )

        category_resource_relationships_parent.additional_properties = d
        return category_resource_relationships_parent

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
