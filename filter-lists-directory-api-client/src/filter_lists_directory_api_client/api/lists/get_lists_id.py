from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.filter_lists_directory_api_contracts_models_list_details_vm import (
    FilterListsDirectoryApiContractsModelsListDetailsVm,
)
from ...models.microsoft_asp_net_core_mvc_problem_details import MicrosoftAspNetCoreMvcProblemDetails
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/lists/{id}".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[FilterListsDirectoryApiContractsModelsListDetailsVm, MicrosoftAspNetCoreMvcProblemDetails]]:
    if response.status_code == 200:
        response_200 = FilterListsDirectoryApiContractsModelsListDetailsVm.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = MicrosoftAspNetCoreMvcProblemDetails.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[FilterListsDirectoryApiContractsModelsListDetailsVm, MicrosoftAspNetCoreMvcProblemDetails]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: Client,
) -> Response[Union[FilterListsDirectoryApiContractsModelsListDetailsVm, MicrosoftAspNetCoreMvcProblemDetails]]:
    """Gets the details of the FilterList.

    Args:
        id (int):

    Returns:
        Response[Union[FilterListsDirectoryApiContractsModelsListDetailsVm, MicrosoftAspNetCoreMvcProblemDetails]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: int,
    *,
    client: Client,
) -> Optional[Union[FilterListsDirectoryApiContractsModelsListDetailsVm, MicrosoftAspNetCoreMvcProblemDetails]]:
    """Gets the details of the FilterList.

    Args:
        id (int):

    Returns:
        Response[Union[FilterListsDirectoryApiContractsModelsListDetailsVm, MicrosoftAspNetCoreMvcProblemDetails]]
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: Client,
) -> Response[Union[FilterListsDirectoryApiContractsModelsListDetailsVm, MicrosoftAspNetCoreMvcProblemDetails]]:
    """Gets the details of the FilterList.

    Args:
        id (int):

    Returns:
        Response[Union[FilterListsDirectoryApiContractsModelsListDetailsVm, MicrosoftAspNetCoreMvcProblemDetails]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: int,
    *,
    client: Client,
) -> Optional[Union[FilterListsDirectoryApiContractsModelsListDetailsVm, MicrosoftAspNetCoreMvcProblemDetails]]:
    """Gets the details of the FilterList.

    Args:
        id (int):

    Returns:
        Response[Union[FilterListsDirectoryApiContractsModelsListDetailsVm, MicrosoftAspNetCoreMvcProblemDetails]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
