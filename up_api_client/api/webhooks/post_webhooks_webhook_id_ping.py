from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.webhook_event_callback import WebhookEventCallback
from ...types import Response


def _get_kwargs(
    webhook_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/webhooks/{webhook_id}/ping".format(
            webhook_id=webhook_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[WebhookEventCallback]:
    if response.status_code == 201:
        response_201 = WebhookEventCallback.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[WebhookEventCallback]:
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
) -> Response[WebhookEventCallback]:
    """Ping webhook

     Send a `PING` event to a webhook by providing its unique identifier.
    This is useful for testing and debugging purposes. The event is delivered
    asynchronously and its data is returned in the response to this request.

    Args:
        webhook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebhookEventCallback]
    """

    kwargs = _get_kwargs(
        webhook_id=webhook_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    webhook_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[WebhookEventCallback]:
    """Ping webhook

     Send a `PING` event to a webhook by providing its unique identifier.
    This is useful for testing and debugging purposes. The event is delivered
    asynchronously and its data is returned in the response to this request.

    Args:
        webhook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebhookEventCallback
    """

    return sync_detailed(
        webhook_id=webhook_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    webhook_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[WebhookEventCallback]:
    """Ping webhook

     Send a `PING` event to a webhook by providing its unique identifier.
    This is useful for testing and debugging purposes. The event is delivered
    asynchronously and its data is returned in the response to this request.

    Args:
        webhook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebhookEventCallback]
    """

    kwargs = _get_kwargs(
        webhook_id=webhook_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    webhook_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[WebhookEventCallback]:
    """Ping webhook

     Send a `PING` event to a webhook by providing its unique identifier.
    This is useful for testing and debugging purposes. The event is delivered
    asynchronously and its data is returned in the response to this request.

    Args:
        webhook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebhookEventCallback
    """

    return (
        await asyncio_detailed(
            webhook_id=webhook_id,
            client=client,
        )
    ).parsed
