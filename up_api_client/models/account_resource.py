from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_resource_attributes import AccountResourceAttributes
    from ..models.account_resource_links import AccountResourceLinks
    from ..models.account_resource_relationships import AccountResourceRelationships


T = TypeVar("T", bound="AccountResource")


@_attrs_define
class AccountResource:
    """Provides information about an Up bank account.

    Attributes:
        type_ (str): The type of this resource: `accounts`
        id (str): The unique identifier for this account.
        attributes (AccountResourceAttributes):
        relationships (AccountResourceRelationships):
        links (Union[Unset, AccountResourceLinks]):
    """

    type_: str
    id: str
    attributes: "AccountResourceAttributes"
    relationships: "AccountResourceRelationships"
    links: Union[Unset, "AccountResourceLinks"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        id = self.id

        attributes = self.attributes.to_dict()

        relationships = self.relationships.to_dict()

        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "id": id,
                "attributes": attributes,
                "relationships": relationships,
            }
        )
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.account_resource_attributes import AccountResourceAttributes
        from ..models.account_resource_links import AccountResourceLinks
        from ..models.account_resource_relationships import AccountResourceRelationships

        d = src_dict.copy()
        type_ = d.pop("type")

        id = d.pop("id")

        attributes = AccountResourceAttributes.from_dict(d.pop("attributes"))

        relationships = AccountResourceRelationships.from_dict(d.pop("relationships"))

        _links = d.pop("links", UNSET)
        links: Union[Unset, AccountResourceLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = AccountResourceLinks.from_dict(_links)

        account_resource = cls(
            type_=type_,
            id=id,
            attributes=attributes,
            relationships=relationships,
            links=links,
        )

        account_resource.additional_properties = d
        return account_resource

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
