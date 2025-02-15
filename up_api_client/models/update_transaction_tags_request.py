from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.tag_input_resource_identifier import TagInputResourceIdentifier


T = TypeVar("T", bound="UpdateTransactionTagsRequest")


@_attrs_define
class UpdateTransactionTagsRequest:
    """Request to add or remove tags associated with a transaction.

    Attributes:
        data (list['TagInputResourceIdentifier']): The tags to add to or remove from the transaction.
    """

    data: list["TagInputResourceIdentifier"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.tag_input_resource_identifier import TagInputResourceIdentifier

        d = src_dict.copy()
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = TagInputResourceIdentifier.from_dict(data_item_data)

            data.append(data_item)

        update_transaction_tags_request = cls(
            data=data,
        )

        update_transaction_tags_request.additional_properties = d
        return update_transaction_tags_request

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
