from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attachment_resource_attributes import AttachmentResourceAttributes
    from ..models.attachment_resource_links import AttachmentResourceLinks
    from ..models.attachment_resource_relationships import (
        AttachmentResourceRelationships,
    )


T = TypeVar("T", bound="AttachmentResource")


@_attrs_define
class AttachmentResource:
    """
    Attributes:
        type_ (str): The type of this resource: `attachments`
        id (str): The unique identifier for this attachment.
        attributes (AttachmentResourceAttributes):
        relationships (AttachmentResourceRelationships):
        links (Union[Unset, AttachmentResourceLinks]):
    """

    type_: str
    id: str
    attributes: "AttachmentResourceAttributes"
    relationships: "AttachmentResourceRelationships"
    links: Union[Unset, "AttachmentResourceLinks"] = UNSET
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
        from ..models.attachment_resource_attributes import AttachmentResourceAttributes
        from ..models.attachment_resource_links import AttachmentResourceLinks
        from ..models.attachment_resource_relationships import (
            AttachmentResourceRelationships,
        )

        d = src_dict.copy()
        type_ = d.pop("type")

        id = d.pop("id")

        attributes = AttachmentResourceAttributes.from_dict(d.pop("attributes"))

        relationships = AttachmentResourceRelationships.from_dict(
            d.pop("relationships")
        )

        _links = d.pop("links", UNSET)
        links: Union[Unset, AttachmentResourceLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = AttachmentResourceLinks.from_dict(_links)

        attachment_resource = cls(
            type_=type_,
            id=id,
            attributes=attributes,
            relationships=relationships,
            links=links,
        )

        attachment_resource.additional_properties = d
        return attachment_resource

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
