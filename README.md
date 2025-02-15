# up@ag

[Up](https://up.com.au) at a glance.


## How to generate a Python client

Up's [api](https://github.com/up-banking/api) repository is referenced as a submodule in the `api` directory.

Generate a Python client from Up's OpenAPI specification using [openapi-python-client](https://github.com/openapi-generators/openapi-python-client):

```shell
uvx openapi-python-client generate --path api/v1/openapi.json --meta none
```

This outputs a Python client package to the [`up_api_client`](up_api_client/) directory.
Running the following script should return ⚡️ from Up's ping [endpoint](https://developer.up.com.au/#get_util_ping):

```python
from up_api_client import AuthenticatedClient
from up_api_client.api.utility_endpoints import get_util_ping

with AuthenticatedClient(
    base_url="https://api.up.com.au/api/v1",
    token="up:yeah:GeVStSMeU3HU4UUxZ5igvaC...ZXGHIKun3W7YyNDAbGRbTFfeU5ys",
) as authenticated_client:
    print(get_util_ping.sync(client=authenticated_client).meta.status_emoji)
```
