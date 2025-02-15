import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_transactions_response import ListTransactionsResponse
from ...models.transaction_status_enum import TransactionStatusEnum
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    pagesize: Union[Unset, int] = UNSET,
    filterstatus: Union[Unset, TransactionStatusEnum] = UNSET,
    filtersince: Union[Unset, datetime.datetime] = UNSET,
    filteruntil: Union[Unset, datetime.datetime] = UNSET,
    filtercategory: Union[Unset, str] = UNSET,
    filtertag: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page[size]"] = pagesize

    json_filterstatus: Union[Unset, str] = UNSET
    if not isinstance(filterstatus, Unset):
        json_filterstatus = filterstatus.value

    params["filter[status]"] = json_filterstatus

    json_filtersince: Union[Unset, str] = UNSET
    if not isinstance(filtersince, Unset):
        json_filtersince = filtersince.isoformat()
    params["filter[since]"] = json_filtersince

    json_filteruntil: Union[Unset, str] = UNSET
    if not isinstance(filteruntil, Unset):
        json_filteruntil = filteruntil.isoformat()
    params["filter[until]"] = json_filteruntil

    params["filter[category]"] = filtercategory

    params["filter[tag]"] = filtertag

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/transactions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ListTransactionsResponse]:
    if response.status_code == 200:
        response_200 = ListTransactionsResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ListTransactionsResponse]:
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
    filterstatus: Union[Unset, TransactionStatusEnum] = UNSET,
    filtersince: Union[Unset, datetime.datetime] = UNSET,
    filteruntil: Union[Unset, datetime.datetime] = UNSET,
    filtercategory: Union[Unset, str] = UNSET,
    filtertag: Union[Unset, str] = UNSET,
) -> Response[ListTransactionsResponse]:
    """List transactions

     Retrieve a list of all transactions across all accounts for the currently
    authenticated user. The returned list is [paginated](#pagination) and can
    be scrolled by following the `next` and `prev` links where present. To
    narrow the results to a specific date range pass one or both of
    `filter[since]` and `filter[until]` in the query string. These filter
    parameters **should not** be used for pagination. Results are ordered
    newest first to oldest last.

    Args:
        pagesize (Union[Unset, int]):
        filterstatus (Union[Unset, TransactionStatusEnum]): Specifies which stage of processing a
            transaction is currently at.
            Currently returned values are `HELD` and `SETTLED`. When a transaction is
            held, its account’s `availableBalance` is affected. When a transaction is
            settled, its account’s `currentBalance` is affected.
        filtersince (Union[Unset, datetime.datetime]):
        filteruntil (Union[Unset, datetime.datetime]):
        filtercategory (Union[Unset, str]):
        filtertag (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListTransactionsResponse]
    """

    kwargs = _get_kwargs(
        pagesize=pagesize,
        filterstatus=filterstatus,
        filtersince=filtersince,
        filteruntil=filteruntil,
        filtercategory=filtercategory,
        filtertag=filtertag,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    pagesize: Union[Unset, int] = UNSET,
    filterstatus: Union[Unset, TransactionStatusEnum] = UNSET,
    filtersince: Union[Unset, datetime.datetime] = UNSET,
    filteruntil: Union[Unset, datetime.datetime] = UNSET,
    filtercategory: Union[Unset, str] = UNSET,
    filtertag: Union[Unset, str] = UNSET,
) -> Optional[ListTransactionsResponse]:
    """List transactions

     Retrieve a list of all transactions across all accounts for the currently
    authenticated user. The returned list is [paginated](#pagination) and can
    be scrolled by following the `next` and `prev` links where present. To
    narrow the results to a specific date range pass one or both of
    `filter[since]` and `filter[until]` in the query string. These filter
    parameters **should not** be used for pagination. Results are ordered
    newest first to oldest last.

    Args:
        pagesize (Union[Unset, int]):
        filterstatus (Union[Unset, TransactionStatusEnum]): Specifies which stage of processing a
            transaction is currently at.
            Currently returned values are `HELD` and `SETTLED`. When a transaction is
            held, its account’s `availableBalance` is affected. When a transaction is
            settled, its account’s `currentBalance` is affected.
        filtersince (Union[Unset, datetime.datetime]):
        filteruntil (Union[Unset, datetime.datetime]):
        filtercategory (Union[Unset, str]):
        filtertag (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListTransactionsResponse
    """

    return sync_detailed(
        client=client,
        pagesize=pagesize,
        filterstatus=filterstatus,
        filtersince=filtersince,
        filteruntil=filteruntil,
        filtercategory=filtercategory,
        filtertag=filtertag,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    pagesize: Union[Unset, int] = UNSET,
    filterstatus: Union[Unset, TransactionStatusEnum] = UNSET,
    filtersince: Union[Unset, datetime.datetime] = UNSET,
    filteruntil: Union[Unset, datetime.datetime] = UNSET,
    filtercategory: Union[Unset, str] = UNSET,
    filtertag: Union[Unset, str] = UNSET,
) -> Response[ListTransactionsResponse]:
    """List transactions

     Retrieve a list of all transactions across all accounts for the currently
    authenticated user. The returned list is [paginated](#pagination) and can
    be scrolled by following the `next` and `prev` links where present. To
    narrow the results to a specific date range pass one or both of
    `filter[since]` and `filter[until]` in the query string. These filter
    parameters **should not** be used for pagination. Results are ordered
    newest first to oldest last.

    Args:
        pagesize (Union[Unset, int]):
        filterstatus (Union[Unset, TransactionStatusEnum]): Specifies which stage of processing a
            transaction is currently at.
            Currently returned values are `HELD` and `SETTLED`. When a transaction is
            held, its account’s `availableBalance` is affected. When a transaction is
            settled, its account’s `currentBalance` is affected.
        filtersince (Union[Unset, datetime.datetime]):
        filteruntil (Union[Unset, datetime.datetime]):
        filtercategory (Union[Unset, str]):
        filtertag (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListTransactionsResponse]
    """

    kwargs = _get_kwargs(
        pagesize=pagesize,
        filterstatus=filterstatus,
        filtersince=filtersince,
        filteruntil=filteruntil,
        filtercategory=filtercategory,
        filtertag=filtertag,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    pagesize: Union[Unset, int] = UNSET,
    filterstatus: Union[Unset, TransactionStatusEnum] = UNSET,
    filtersince: Union[Unset, datetime.datetime] = UNSET,
    filteruntil: Union[Unset, datetime.datetime] = UNSET,
    filtercategory: Union[Unset, str] = UNSET,
    filtertag: Union[Unset, str] = UNSET,
) -> Optional[ListTransactionsResponse]:
    """List transactions

     Retrieve a list of all transactions across all accounts for the currently
    authenticated user. The returned list is [paginated](#pagination) and can
    be scrolled by following the `next` and `prev` links where present. To
    narrow the results to a specific date range pass one or both of
    `filter[since]` and `filter[until]` in the query string. These filter
    parameters **should not** be used for pagination. Results are ordered
    newest first to oldest last.

    Args:
        pagesize (Union[Unset, int]):
        filterstatus (Union[Unset, TransactionStatusEnum]): Specifies which stage of processing a
            transaction is currently at.
            Currently returned values are `HELD` and `SETTLED`. When a transaction is
            held, its account’s `availableBalance` is affected. When a transaction is
            settled, its account’s `currentBalance` is affected.
        filtersince (Union[Unset, datetime.datetime]):
        filteruntil (Union[Unset, datetime.datetime]):
        filtercategory (Union[Unset, str]):
        filtertag (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListTransactionsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            pagesize=pagesize,
            filterstatus=filterstatus,
            filtersince=filtersince,
            filteruntil=filteruntil,
            filtercategory=filtercategory,
            filtertag=filtertag,
        )
    ).parsed
