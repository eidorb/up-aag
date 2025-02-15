from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.error_object import ErrorObject


T = TypeVar("T", bound="ErrorResponse")


@_attrs_define
class ErrorResponse:
    """Generic error response that returns one or more errors.

    Attributes:
        errors (list['ErrorObject']): The list of errors returned in this response.
    """

    errors: list["ErrorObject"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errors = []
        for errors_item_data in self.errors:
            errors_item = errors_item_data.to_dict()
            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.error_object import ErrorObject

        d = src_dict.copy()
        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:
            errors_item = ErrorObject.from_dict(errors_item_data)

            errors.append(errors_item)

        error_response = cls(
            errors=errors,
        )

        error_response.additional_properties = d
        return error_response

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
