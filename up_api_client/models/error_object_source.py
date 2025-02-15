from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ErrorObjectSource")


@_attrs_define
class ErrorObjectSource:
    """If applicable, location in the request that this error relates to. This
    may be a parameter in the query string, or a an attribute in the
    request body.

        Attributes:
            parameter (Union[Unset, str]): If this error relates to a query parameter, the name of the
                parameter.
            pointer (Union[Unset, str]): If this error relates to an attribute in the request body, a
                rfc-6901 JSON pointer to the attribute.
    """

    parameter: Union[Unset, str] = UNSET
    pointer: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parameter = self.parameter

        pointer = self.pointer

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if parameter is not UNSET:
            field_dict["parameter"] = parameter
        if pointer is not UNSET:
            field_dict["pointer"] = pointer

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        parameter = d.pop("parameter", UNSET)

        pointer = d.pop("pointer", UNSET)

        error_object_source = cls(
            parameter=parameter,
            pointer=pointer,
        )

        error_object_source.additional_properties = d
        return error_object_source

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
