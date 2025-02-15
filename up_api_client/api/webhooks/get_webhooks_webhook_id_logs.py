from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_webhook_delivery_logs_response import (
    ListWebhookDeliveryLogsResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    webhook_id: str,
    *,
    pagesize: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page[size]"] = pagesize

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webhooks/{webhook_id}/logs".format(
            webhook_id=webhook_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ListWebhookDeliveryLogsResponse]:
    if response.status_code == 200:
        response_200 = ListWebhookDeliveryLogsResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ListWebhookDeliveryLogsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    webhook_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    pagesize: Union[Unset, int] = UNSET,
) -> Response[ListWebhookDeliveryLogsResponse]:
    """List webhook logs

     Retrieve a list of delivery logs for a webhook by providing its unique
    identifier. This is useful for analysis and debugging purposes. The
    returned list is [paginated](#pagination) and can be scrolled by
    following the `next` and `prev` links where present. Results are ordered
    newest first to oldest last. Logs may be automatically purged after a
    period of time.

    Args:
        webhook_id (str):
        pagesize (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListWebhookDeliveryLogsResponse]
    """

    kwargs = _get_kwargs(
        webhook_id=webhook_id,
        pagesize=pagesize,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    webhook_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    pagesize: Union[Unset, int] = UNSET,
) -> Optional[ListWebhookDeliveryLogsResponse]:
    """List webhook logs

     Retrieve a list of delivery logs for a webhook by providing its unique
    identifier. This is useful for analysis and debugging purposes. The
    returned list is [paginated](#pagination) and can be scrolled by
    following the `next` and `prev` links where present. Results are ordered
    newest first to oldest last. Logs may be automatically purged after a
    period of time.

    Args:
        webhook_id (str):
        pagesize (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListWebhookDeliveryLogsResponse
    """

    return sync_detailed(
        webhook_id=webhook_id,
        client=client,
        pagesize=pagesize,
    ).parsed


async def asyncio_detailed(
    webhook_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    pagesize: Union[Unset, int] = UNSET,
) -> Response[ListWebhookDeliveryLogsResponse]:
    """List webhook logs

     Retrieve a list of delivery logs for a webhook by providing its unique
    identifier. This is useful for analysis and debugging purposes. The
    returned list is [paginated](#pagination) and can be scrolled by
    following the `next` and `prev` links where present. Results are ordered
    newest first to oldest last. Logs may be automatically purged after a
    period of time.

    Args:
        webhook_id (str):
        pagesize (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListWebhookDeliveryLogsResponse]
    """

    kwargs = _get_kwargs(
        webhook_id=webhook_id,
        pagesize=pagesize,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    webhook_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    pagesize: Union[Unset, int] = UNSET,
) -> Optional[ListWebhookDeliveryLogsResponse]:
    """List webhook logs

     Retrieve a list of delivery logs for a webhook by providing its unique
    identifier. This is useful for analysis and debugging purposes. The
    returned list is [paginated](#pagination) and can be scrolled by
    following the `next` and `prev` links where present. Results are ordered
    newest first to oldest last. Logs may be automatically purged after a
    period of time.

    Args:
        webhook_id (str):
        pagesize (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListWebhookDeliveryLogsResponse
    """

    return (
        await asyncio_detailed(
            webhook_id=webhook_id,
            client=client,
            pagesize=pagesize,
        )
    ).parsed
