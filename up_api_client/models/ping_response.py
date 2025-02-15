from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.ping_response_meta import PingResponseMeta


T = TypeVar("T", bound="PingResponse")


@_attrs_define
class PingResponse:
    """Basic ping response to verify authentication.

    Attributes:
        meta (PingResponseMeta):
    """

    meta: "PingResponseMeta"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "meta": meta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.ping_response_meta import PingResponseMeta

        d = src_dict.copy()
        meta = PingResponseMeta.from_dict(d.pop("meta"))

        ping_response = cls(
            meta=meta,
        )

        ping_response.additional_properties = d
        return ping_response

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
