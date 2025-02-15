from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_webhook_request import CreateWebhookRequest
from ...models.create_webhook_response import CreateWebhookResponse
from ...types import Response


def _get_kwargs(
    *,
    body: CreateWebhookRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/webhooks",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CreateWebhookResponse]:
    if response.status_code == 201:
        response_201 = CreateWebhookResponse.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CreateWebhookResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateWebhookRequest,
) -> Response[CreateWebhookResponse]:
    """Create webhook

     Create a new webhook with a given URL. The URL will receive webhook
    events as JSON-encoded `POST` requests. The URL must respond with a HTTP
    `200` status on success.

    There is currently a limit of 10 webhooks at any given time. Once this
    limit is reached, existing webhooks will need to be deleted before new
    webhooks can be created.

    Event delivery is retried with exponential backoff if the URL is
    unreachable or it does not respond with a `200` status. The response
    includes a `secretKey` attribute, which is used to sign requests sent to
    the webhook URL. It will not be returned from any other endpoints within
    the Up API. If the `secretKey` is lost, simply create a new webhook with
    the same URL, capture its `secretKey` and then delete the original
    webhook. See [Handling webhook events](#callback_post_webhookURL) for
    details on how to process webhook events.

    It is probably a good idea to test the webhook by
    [sending it a `PING` event](#post_webhooks_webhookId_ping) after creating
    it.

    Args:
        body (CreateWebhookRequest): Request to create a new webhook. This currently only requires
            a `url`
            attribute.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateWebhookResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateWebhookRequest,
) -> Optional[CreateWebhookResponse]:
    """Create webhook

     Create a new webhook with a given URL. The URL will receive webhook
    events as JSON-encoded `POST` requests. The URL must respond with a HTTP
    `200` status on success.

    There is currently a limit of 10 webhooks at any given time. Once this
    limit is reached, existing webhooks will need to be deleted before new
    webhooks can be created.

    Event delivery is retried with exponential backoff if the URL is
    unreachable or it does not respond with a `200` status. The response
    includes a `secretKey` attribute, which is used to sign requests sent to
    the webhook URL. It will not be returned from any other endpoints within
    the Up API. If the `secretKey` is lost, simply create a new webhook with
    the same URL, capture its `secretKey` and then delete the original
    webhook. See [Handling webhook events](#callback_post_webhookURL) for
    details on how to process webhook events.

    It is probably a good idea to test the webhook by
    [sending it a `PING` event](#post_webhooks_webhookId_ping) after creating
    it.

    Args:
        body (CreateWebhookRequest): Request to create a new webhook. This currently only requires
            a `url`
            attribute.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateWebhookResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateWebhookRequest,
) -> Response[CreateWebhookResponse]:
    """Create webhook

     Create a new webhook with a given URL. The URL will receive webhook
    events as JSON-encoded `POST` requests. The URL must respond with a HTTP
    `200` status on success.

    There is currently a limit of 10 webhooks at any given time. Once this
    limit is reached, existing webhooks will need to be deleted before new
    webhooks can be created.

    Event delivery is retried with exponential backoff if the URL is
    unreachable or it does not respond with a `200` status. The response
    includes a `secretKey` attribute, which is used to sign requests sent to
    the webhook URL. It will not be returned from any other endpoints within
    the Up API. If the `secretKey` is lost, simply create a new webhook with
    the same URL, capture its `secretKey` and then delete the original
    webhook. See [Handling webhook events](#callback_post_webhookURL) for
    details on how to process webhook events.

    It is probably a good idea to test the webhook by
    [sending it a `PING` event](#post_webhooks_webhookId_ping) after creating
    it.

    Args:
        body (CreateWebhookRequest): Request to create a new webhook. This currently only requires
            a `url`
            attribute.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateWebhookResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateWebhookRequest,
) -> Optional[CreateWebhookResponse]:
    """Create webhook

     Create a new webhook with a given URL. The URL will receive webhook
    events as JSON-encoded `POST` requests. The URL must respond with a HTTP
    `200` status on success.

    There is currently a limit of 10 webhooks at any given time. Once this
    limit is reached, existing webhooks will need to be deleted before new
    webhooks can be created.

    Event delivery is retried with exponential backoff if the URL is
    unreachable or it does not respond with a `200` status. The response
    includes a `secretKey` attribute, which is used to sign requests sent to
    the webhook URL. It will not be returned from any other endpoints within
    the Up API. If the `secretKey` is lost, simply create a new webhook with
    the same URL, capture its `secretKey` and then delete the original
    webhook. See [Handling webhook events](#callback_post_webhookURL) for
    details on how to process webhook events.

    It is probably a good idea to test the webhook by
    [sending it a `PING` event](#post_webhooks_webhookId_ping) after creating
    it.

    Args:
        body (CreateWebhookRequest): Request to create a new webhook. This currently only requires
            a `url`
            attribute.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateWebhookResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
