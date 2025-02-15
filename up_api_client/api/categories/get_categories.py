from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_categories_response import ListCategoriesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    filterparent: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["filter[parent]"] = filterparent

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/categories",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ListCategoriesResponse]:
    if response.status_code == 200:
        response_200 = ListCategoriesResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ListCategoriesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    filterparent: Union[Unset, str] = UNSET,
) -> Response[ListCategoriesResponse]:
    """List categories

     Retrieve a list of all categories and their ancestry. The returned list
    is not paginated.

    Args:
        filterparent (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListCategoriesResponse]
    """

    kwargs = _get_kwargs(
        filterparent=filterparent,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    filterparent: Union[Unset, str] = UNSET,
) -> Optional[ListCategoriesResponse]:
    """List categories

     Retrieve a list of all categories and their ancestry. The returned list
    is not paginated.

    Args:
        filterparent (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListCategoriesResponse
    """

    return sync_detailed(
        client=client,
        filterparent=filterparent,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    filterparent: Union[Unset, str] = UNSET,
) -> Response[ListCategoriesResponse]:
    """List categories

     Retrieve a list of all categories and their ancestry. The returned list
    is not paginated.

    Args:
        filterparent (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListCategoriesResponse]
    """

    kwargs = _get_kwargs(
        filterparent=filterparent,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    filterparent: Union[Unset, str] = UNSET,
) -> Optional[ListCategoriesResponse]:
    """List categories

     Retrieve a list of all categories and their ancestry. The returned list
    is not paginated.

    Args:
        filterparent (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListCategoriesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            filterparent=filterparent,
        )
    ).parsed
