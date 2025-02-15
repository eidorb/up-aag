from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_webhooks_response import ListWebhooksResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    pagesize: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page[size]"] = pagesize

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webhooks",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ListWebhooksResponse]:
    if response.status_code == 200:
        response_200 = ListWebhooksResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ListWebhooksResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    pagesize: Union[Unset, int] = UNSET,
) -> Response[ListWebhooksResponse]:
    """List webhooks

     Retrieve a list of configured webhooks. The returned list is
    [paginated](#pagination) and can be scrolled by following the `next`
    and `prev` links where present. Results are ordered oldest first to
    newest last.

    Args:
        pagesize (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListWebhooksResponse]
    """

    kwargs = _get_kwargs(
        pagesize=pagesize,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    pagesize: Union[Unset, int] = UNSET,
) -> Optional[ListWebhooksResponse]:
    """List webhooks

     Retrieve a list of configured webhooks. The returned list is
    [paginated](#pagination) and can be scrolled by following the `next`
    and `prev` links where present. Results are ordered oldest first to
    newest last.

    Args:
        pagesize (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListWebhooksResponse
    """

    return sync_detailed(
        client=client,
        pagesize=pagesize,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    pagesize: Union[Unset, int] = UNSET,
) -> Response[ListWebhooksResponse]:
    """List webhooks

     Retrieve a list of configured webhooks. The returned list is
    [paginated](#pagination) and can be scrolled by following the `next`
    and `prev` links where present. Results are ordered oldest first to
    newest last.

    Args:
        pagesize (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListWebhooksResponse]
    """

    kwargs = _get_kwargs(
        pagesize=pagesize,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    pagesize: Union[Unset, int] = UNSET,
) -> Optional[ListWebhooksResponse]:
    """List webhooks

     Retrieve a list of configured webhooks. The returned list is
    [paginated](#pagination) and can be scrolled by following the `next`
    and `prev` links where present. Results are ordered oldest first to
    newest last.

    Args:
        pagesize (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListWebhooksResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            pagesize=pagesize,
        )
    ).parsed
