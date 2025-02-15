import datetime
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookResourceAttributes")


@_attrs_define
class WebhookResourceAttributes:
    """
    Attributes:
        url (str): The URL that this webhook is configured to `POST` events to.
        description (Union[None, str]): An optional description that was provided at the time the webhook was
            created.
        created_at (datetime.datetime): The date-time at which this webhook was created.
        secret_key (Union[Unset, str]): A shared secret key used to sign all webhook events sent to the
            configured webhook URL. This field is returned only once, upon the
            initial creation of the webhook. If lost, create a new webhook and
            delete this webhook.

            The webhook URL receives a request with a
            `X-Up-Authenticity-Signature` header, which is the SHA-256 HMAC of
            the entire raw request body signed using this `secretKey`. It is
            advised to compute and check this signature to verify the
            authenticity of requests sent to the webhook URL. See
            [Handling webhook events](#callback_post_webhookURL) for full
            details.
    """

    url: str
    description: Union[None, str]
    created_at: datetime.datetime
    secret_key: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        description: Union[None, str]
        description = self.description

        created_at = self.created_at.isoformat()

        secret_key = self.secret_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "description": description,
                "createdAt": created_at,
            }
        )
        if secret_key is not UNSET:
            field_dict["secretKey"] = secret_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        def _parse_description(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        description = _parse_description(d.pop("description"))

        created_at = isoparse(d.pop("createdAt"))

        secret_key = d.pop("secretKey", UNSET)

        webhook_resource_attributes = cls(
            url=url,
            description=description,
            created_at=created_at,
            secret_key=secret_key,
        )

        webhook_resource_attributes.additional_properties = d
        return webhook_resource_attributes

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
