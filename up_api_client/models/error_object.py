from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_object_source import ErrorObjectSource


T = TypeVar("T", bound="ErrorObject")


@_attrs_define
class ErrorObject:
    """Provides information about an error processing a request.

    Attributes:
        status (str): The HTTP status code associated with this error. This can also be
            obtained from the response headers. The status indicates the broad type
            of error according to HTTP semantics.
        title (str): A short description of this error. This should be stable across
            multiple occurrences of this type of error and typically expands on the
            reason for the status code.
        detail (str): A detailed description of this error. This should be considered unique
            to individual occurrences of an error and subject to change. It is
            useful for debugging purposes.
        source (Union[Unset, ErrorObjectSource]): If applicable, location in the request that this error relates to.
            This
            may be a parameter in the query string, or a an attribute in the
            request body.
    """

    status: str
    title: str
    detail: str
    source: Union[Unset, "ErrorObjectSource"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        title = self.title

        detail = self.detail

        source: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "title": title,
                "detail": detail,
            }
        )
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.error_object_source import ErrorObjectSource

        d = src_dict.copy()
        status = d.pop("status")

        title = d.pop("title")

        detail = d.pop("detail")

        _source = d.pop("source", UNSET)
        source: Union[Unset, ErrorObjectSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = ErrorObjectSource.from_dict(_source)

        error_object = cls(
            status=status,
            title=title,
            detail=detail,
            source=source,
        )

        error_object.additional_properties = d
        return error_object

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
