import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.webhook_delivery_status_enum import WebhookDeliveryStatusEnum

if TYPE_CHECKING:
    from ..models.webhook_delivery_log_resource_attributes_request import (
        WebhookDeliveryLogResourceAttributesRequest,
    )
    from ..models.webhook_delivery_log_resource_attributes_response_type_0 import (
        WebhookDeliveryLogResourceAttributesResponseType0,
    )


T = TypeVar("T", bound="WebhookDeliveryLogResourceAttributes")


@_attrs_define
class WebhookDeliveryLogResourceAttributes:
    """
    Attributes:
        request (WebhookDeliveryLogResourceAttributesRequest): Information about the request that was sent to the
            webhook URL.
        response (Union['WebhookDeliveryLogResourceAttributesResponseType0', None]): Information about the response that
            was received from the webhook URL.
        delivery_status (WebhookDeliveryStatusEnum): Specifies the nature of the success or failure of a webhook
            delivery
            attempt to the subscribed webhook URL. The currently returned values are
            described below:

            - **`DELIVERED`**: The event was delivered to the webhook URL
              successfully and a `200` response was received.
            - **`UNDELIVERABLE`**: The webhook URL was not reachable, or timed out.
            - **`BAD_RESPONSE_CODE`**: The event was delivered to the webhook URL
              but a non-`200` response was received.
        created_at (datetime.datetime): The date-time at which this log entry was created.
    """

    request: "WebhookDeliveryLogResourceAttributesRequest"
    response: Union["WebhookDeliveryLogResourceAttributesResponseType0", None]
    delivery_status: WebhookDeliveryStatusEnum
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.webhook_delivery_log_resource_attributes_response_type_0 import (
            WebhookDeliveryLogResourceAttributesResponseType0,
        )

        request = self.request.to_dict()

        response: Union[None, dict[str, Any]]
        if isinstance(self.response, WebhookDeliveryLogResourceAttributesResponseType0):
            response = self.response.to_dict()
        else:
            response = self.response

        delivery_status = self.delivery_status.value

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "request": request,
                "response": response,
                "deliveryStatus": delivery_status,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.webhook_delivery_log_resource_attributes_request import (
            WebhookDeliveryLogResourceAttributesRequest,
        )
        from ..models.webhook_delivery_log_resource_attributes_response_type_0 import (
            WebhookDeliveryLogResourceAttributesResponseType0,
        )

        d = src_dict.copy()
        request = WebhookDeliveryLogResourceAttributesRequest.from_dict(
            d.pop("request")
        )

        def _parse_response(
            data: object,
        ) -> Union["WebhookDeliveryLogResourceAttributesResponseType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_type_0 = (
                    WebhookDeliveryLogResourceAttributesResponseType0.from_dict(data)
                )

                return response_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union["WebhookDeliveryLogResourceAttributesResponseType0", None], data
            )

        response = _parse_response(d.pop("response"))

        delivery_status = WebhookDeliveryStatusEnum(d.pop("deliveryStatus"))

        created_at = isoparse(d.pop("createdAt"))

        webhook_delivery_log_resource_attributes = cls(
            request=request,
            response=response,
            delivery_status=delivery_status,
            created_at=created_at,
        )

        webhook_delivery_log_resource_attributes.additional_properties = d
        return webhook_delivery_log_resource_attributes

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
