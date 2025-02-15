from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_transaction_tags_request import UpdateTransactionTagsRequest
from ...types import Response


def _get_kwargs(
    transaction_id: str,
    *,
    body: UpdateTransactionTagsRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/transactions/{transaction_id}/relationships/tags".format(
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
    body: UpdateTransactionTagsRequest,
) -> Response[Any]:
    """Remove tags from transaction

     Disassociates one or more tags from a specific transaction. Tags that are
    not associated are silently ignored. An HTTP `204` is returned on
    success. The associated tags, along with this request URL, are also
    exposed via the `tags` relationship on the transaction resource returned
    from `/transactions/{id}`.

    Args:
        transaction_id (str):
        body (UpdateTransactionTagsRequest): Request to add or remove tags associated with a
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
    body: UpdateTransactionTagsRequest,
) -> Response[Any]:
    """Remove tags from transaction

     Disassociates one or more tags from a specific transaction. Tags that are
    not associated are silently ignored. An HTTP `204` is returned on
    success. The associated tags, along with this request URL, are also
    exposed via the `tags` relationship on the transaction resource returned
    from `/transactions/{id}`.

    Args:
        transaction_id (str):
        body (UpdateTransactionTagsRequest): Request to add or remove tags associated with a
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
