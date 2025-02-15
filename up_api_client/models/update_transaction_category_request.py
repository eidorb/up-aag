from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.category_input_resource_identifier import (
        CategoryInputResourceIdentifier,
    )


T = TypeVar("T", bound="UpdateTransactionCategoryRequest")


@_attrs_define
class UpdateTransactionCategoryRequest:
    """Request to update the category associated with a transaction.

    Attributes:
        data (Union['CategoryInputResourceIdentifier', None]): The category to set on the transaction. Set this entire
            key to `null`
            de-categorize a transaction.
    """

    data: Union["CategoryInputResourceIdentifier", None]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.category_input_resource_identifier import (
            CategoryInputResourceIdentifier,
        )

        data: Union[None, dict[str, Any]]
        if isinstance(self.data, CategoryInputResourceIdentifier):
            data = self.data.to_dict()
        else:
            data = self.data

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
        from ..models.category_input_resource_identifier import (
            CategoryInputResourceIdentifier,
        )

        d = src_dict.copy()

        def _parse_data(data: object) -> Union["CategoryInputResourceIdentifier", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_1 = CategoryInputResourceIdentifier.from_dict(data)

                return data_type_1
            except:  # noqa: E722
                pass
            return cast(Union["CategoryInputResourceIdentifier", None], data)

        data = _parse_data(d.pop("data"))

        update_transaction_category_request = cls(
            data=data,
        )

        update_transaction_category_request.additional_properties = d
        return update_transaction_category_request

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
