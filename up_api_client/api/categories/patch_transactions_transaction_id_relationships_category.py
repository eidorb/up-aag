from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_transaction_category_request import (
    UpdateTransactionCategoryRequest,
)
from ...types import Response


def _get_kwargs(
    transaction_id: str,
    *,
    body: UpdateTransactionCategoryRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/transactions/{transaction_id}/relationships/category".format(
            transaction_id=transaction_id,
        ),
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Any]:
    if response.status_code == 204:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    transaction_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateTransactionCategoryRequest,
) -> Response[Any]:
    """Categorize transaction

     Updates the category associated with a transaction. Only transactions
    for which `isCategorizable` is set to true support this operation. The
    `id` is taken from the list exposed on `/categories` and cannot be one of
    the top-level (parent) categories. To de-categorize a transaction, set
    the entire `data` key to `null`. An HTTP `204` is returned on success.
    The associated category, along with its request URL is also exposed via
    the `category` relationship on the transaction resource returned from
    `/transactions/{id}`.

    Args:
        transaction_id (str):
        body (UpdateTransactionCategoryRequest): Request to update the category associated with a
            transaction.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        transaction_id=transaction_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    transaction_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateTransactionCategoryRequest,
) -> Response[Any]:
    """Categorize transaction

     Updates the category associated with a transaction. Only transactions
    for which `isCategorizable` is set to true support this operation. The
    `id` is taken from the list exposed on `/categories` and cannot be one of
    the top-level (parent) categories. To de-categorize a transaction, set
    the entire `data` key to `null`. An HTTP `204` is returned on success.
    The associated category, along with its request URL is also exposed via
    the `category` relationship on the transaction resource returned from
    `/transactions/{id}`.

    Args:
        transaction_id (str):
        body (UpdateTransactionCategoryRequest): Request to update the category associated with a
            transaction.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        transaction_id=transaction_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
