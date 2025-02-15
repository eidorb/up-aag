import datetime
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="AttachmentResourceAttributes")


@_attrs_define
class AttachmentResourceAttributes:
    """
    Attributes:
        created_at (Union[None, datetime.datetime]): The date-time when the file was created.
        file_url (Union[None, str]): A temporary link to download the file.
        file_url_expires_at (datetime.datetime): The date-time at which the `fileURL` link expires.
        file_extension (Union[None, str]): File extension for the uploaded attachment.
        file_content_type (Union[None, str]): Content type for the uploaded attachment.
    """

    created_at: Union[None, datetime.datetime]
    file_url: Union[None, str]
    file_url_expires_at: datetime.datetime
    file_extension: Union[None, str]
    file_content_type: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at: Union[None, str]
        if isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        file_url: Union[None, str]
        file_url = self.file_url

        file_url_expires_at = self.file_url_expires_at.isoformat()

        file_extension: Union[None, str]
        file_extension = self.file_extension

        file_content_type: Union[None, str]
        file_content_type = self.file_content_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "fileURL": file_url,
                "fileURLExpiresAt": file_url_expires_at,
                "fileExtension": file_extension,
                "fileContentType": file_content_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_created_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = isoparse(data)

                return created_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        created_at = _parse_created_at(d.pop("createdAt"))

        def _parse_file_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        file_url = _parse_file_url(d.pop("fileURL"))

        file_url_expires_at = isoparse(d.pop("fileURLExpiresAt"))

        def _parse_file_extension(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        file_extension = _parse_file_extension(d.pop("fileExtension"))

        def _parse_file_content_type(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        file_content_type = _parse_file_content_type(d.pop("fileContentType"))

        attachment_resource_attributes = cls(
            created_at=created_at,
            file_url=file_url,
            file_url_expires_at=file_url_expires_at,
            file_extension=file_extension,
            file_content_type=file_content_type,
        )

        attachment_resource_attributes.additional_properties = d
        return attachment_resource_attributes

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
