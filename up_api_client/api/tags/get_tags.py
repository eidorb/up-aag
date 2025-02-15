from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_tags_response import ListTagsResponse
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
        "url": "/tags",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ListTagsResponse]:
    if response.status_code == 200:
        response_200 = ListTagsResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ListTagsResponse]:
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
) -> Response[ListTagsResponse]:
    """List tags

     Retrieve a list of all tags currently in use. The returned list is
    [paginated](#pagination) and can be scrolled by following the `next`
    and `prev` links where present. Results are ordered lexicographically.
    The `transactions` relationship for each tag exposes a link
    to get the transactions with the given tag.

    Args:
        pagesize (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListTagsResponse]
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
) -> Optional[ListTagsResponse]:
    """List tags

     Retrieve a list of all tags currently in use. The returned list is
    [paginated](#pagination) and can be scrolled by following the `next`
    and `prev` links where present. Results are ordered lexicographically.
    The `transactions` relationship for each tag exposes a link
    to get the transactions with the given tag.

    Args:
        pagesize (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListTagsResponse
    """

    return sync_detailed(
        client=client,
        pagesize=pagesize,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    pagesize: Union[Unset, int] = UNSET,
) -> Response[ListTagsResponse]:
    """List tags

     Retrieve a list of all tags currently in use. The returned list is
    [paginated](#pagination) and can be scrolled by following the `next`
    and `prev` links where present. Results are ordered lexicographically.
    The `transactions` relationship for each tag exposes a link
    to get the transactions with the given tag.

    Args:
        pagesize (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListTagsResponse]
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
) -> Optional[ListTagsResponse]:
    """List tags

     Retrieve a list of all tags currently in use. The returned list is
    [paginated](#pagination) and can be scrolled by following the `next`
    and `prev` links where present. Results are ordered lexicographically.
    The `transactions` relationship for each tag exposes a link
    to get the transactions with the given tag.

    Args:
        pagesize (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListTagsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            pagesize=pagesize,
        )
    ).parsed
