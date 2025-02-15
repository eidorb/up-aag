from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transaction_resource_relationships_category_data_type_0 import (
        TransactionResourceRelationshipsCategoryDataType0,
    )
    from ..models.transaction_resource_relationships_category_links import (
        TransactionResourceRelationshipsCategoryLinks,
    )


T = TypeVar("T", bound="TransactionResourceRelationshipsCategory")


@_attrs_define
class TransactionResourceRelationshipsCategory:
    """
    Attributes:
        data (Union['TransactionResourceRelationshipsCategoryDataType0', None]):
        links (Union[Unset, TransactionResourceRelationshipsCategoryLinks]):
    """

    data: Union["TransactionResourceRelationshipsCategoryDataType0", None]
    links: Union[Unset, "TransactionResourceRelationshipsCategoryLinks"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.transaction_resource_relationships_category_data_type_0 import (
            TransactionResourceRelationshipsCategoryDataType0,
        )

        data: Union[None, dict[str, Any]]
        if isinstance(self.data, TransactionResourceRelationshipsCategoryDataType0):
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
        from ..models.transaction_resource_relationships_category_data_type_0 import (
            TransactionResourceRelationshipsCategoryDataType0,
        )
        from ..models.transaction_resource_relationships_category_links import (
            TransactionResourceRelationshipsCategoryLinks,
        )

        d = src_dict.copy()

        def _parse_data(
            data: object,
        ) -> Union["TransactionResourceRelationshipsCategoryDataType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = (
                    TransactionResourceRelationshipsCategoryDataType0.from_dict(data)
                )

                return data_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union["TransactionResourceRelationshipsCategoryDataType0", None], data
            )

        data = _parse_data(d.pop("data"))

        _links = d.pop("links", UNSET)
        links: Union[Unset, TransactionResourceRelationshipsCategoryLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = TransactionResourceRelationshipsCategoryLinks.from_dict(_links)

        transaction_resource_relationships_category = cls(
            data=data,
            links=links,
        )

        transaction_resource_relationships_category.additional_properties = d
        return transaction_resource_relationships_category

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
