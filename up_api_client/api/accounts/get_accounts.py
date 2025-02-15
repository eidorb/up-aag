from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.account_type_enum import AccountTypeEnum
from ...models.list_accounts_response import ListAccountsResponse
from ...models.ownership_type_enum import OwnershipTypeEnum
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    pagesize: Union[Unset, int] = UNSET,
    filteraccount_type: Union[Unset, AccountTypeEnum] = UNSET,
    filterownership_type: Union[Unset, OwnershipTypeEnum] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page[size]"] = pagesize

    json_filteraccount_type: Union[Unset, str] = UNSET
    if not isinstance(filteraccount_type, Unset):
        json_filteraccount_type = filteraccount_type.value

    params["filter[accountType]"] = json_filteraccount_type

    json_filterownership_type: Union[Unset, str] = UNSET
    if not isinstance(filterownership_type, Unset):
        json_filterownership_type = filterownership_type.value

    params["filter[ownershipType]"] = json_filterownership_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/accounts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ListAccountsResponse]:
    if response.status_code == 200:
        response_200 = ListAccountsResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ListAccountsResponse]:
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
    filteraccount_type: Union[Unset, AccountTypeEnum] = UNSET,
    filterownership_type: Union[Unset, OwnershipTypeEnum] = UNSET,
) -> Response[ListAccountsResponse]:
    """List accounts

     Retrieve a paginated list of all accounts for the currently
    authenticated user. The returned list is paginated and can be scrolled
    by following the `prev` and `next` links where present.

    Args:
        pagesize (Union[Unset, int]):
        filteraccount_type (Union[Unset, AccountTypeEnum]): Specifies the type of bank account.
            Currently returned values are
            `SAVER`, `TRANSACTIONAL` and `HOME_LOAN`.
        filterownership_type (Union[Unset, OwnershipTypeEnum]): Specifies the structure under
            which a bank account is owned. Currently
            returned values are `INDIVIDUAL` and `JOINT`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListAccountsResponse]
    """

    kwargs = _get_kwargs(
        pagesize=pagesize,
        filteraccount_type=filteraccount_type,
        filterownership_type=filterownership_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    pagesize: Union[Unset, int] = UNSET,
    filteraccount_type: Union[Unset, AccountTypeEnum] = UNSET,
    filterownership_type: Union[Unset, OwnershipTypeEnum] = UNSET,
) -> Optional[ListAccountsResponse]:
    """List accounts

     Retrieve a paginated list of all accounts for the currently
    authenticated user. The returned list is paginated and can be scrolled
    by following the `prev` and `next` links where present.

    Args:
        pagesize (Union[Unset, int]):
        filteraccount_type (Union[Unset, AccountTypeEnum]): Specifies the type of bank account.
            Currently returned values are
            `SAVER`, `TRANSACTIONAL` and `HOME_LOAN`.
        filterownership_type (Union[Unset, OwnershipTypeEnum]): Specifies the structure under
            which a bank account is owned. Currently
            returned values are `INDIVIDUAL` and `JOINT`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListAccountsResponse
    """

    return sync_detailed(
        client=client,
        pagesize=pagesize,
        filteraccount_type=filteraccount_type,
        filterownership_type=filterownership_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    pagesize: Union[Unset, int] = UNSET,
    filteraccount_type: Union[Unset, AccountTypeEnum] = UNSET,
    filterownership_type: Union[Unset, OwnershipTypeEnum] = UNSET,
) -> Response[ListAccountsResponse]:
    """List accounts

     Retrieve a paginated list of all accounts for the currently
    authenticated user. The returned list is paginated and can be scrolled
    by following the `prev` and `next` links where present.

    Args:
        pagesize (Union[Unset, int]):
        filteraccount_type (Union[Unset, AccountTypeEnum]): Specifies the type of bank account.
            Currently returned values are
            `SAVER`, `TRANSACTIONAL` and `HOME_LOAN`.
        filterownership_type (Union[Unset, OwnershipTypeEnum]): Specifies the structure under
            which a bank account is owned. Currently
            returned values are `INDIVIDUAL` and `JOINT`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListAccountsResponse]
    """

    kwargs = _get_kwargs(
        pagesize=pagesize,
        filteraccount_type=filteraccount_type,
        filterownership_type=filterownership_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    pagesize: Union[Unset, int] = UNSET,
    filteraccount_type: Union[Unset, AccountTypeEnum] = UNSET,
    filterownership_type: Union[Unset, OwnershipTypeEnum] = UNSET,
) -> Optional[ListAccountsResponse]:
    """List accounts

     Retrieve a paginated list of all accounts for the currently
    authenticated user. The returned list is paginated and can be scrolled
    by following the `prev` and `next` links where present.

    Args:
        pagesize (Union[Unset, int]):
        filteraccount_type (Union[Unset, AccountTypeEnum]): Specifies the type of bank account.
            Currently returned values are
            `SAVER`, `TRANSACTIONAL` and `HOME_LOAN`.
        filterownership_type (Union[Unset, OwnershipTypeEnum]): Specifies the structure under
            which a bank account is owned. Currently
            returned values are `INDIVIDUAL` and `JOINT`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListAccountsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            pagesize=pagesize,
            filteraccount_type=filteraccount_type,
            filterownership_type=filterownership_type,
        )
    ).parsed
