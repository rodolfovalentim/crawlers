from typing import Any, Dict, List, Optional

import httpx

from ...client import Client
from ...models.filter_lists_directory_application_queries_get_languages_language_vm import (
    FilterListsDirectoryApplicationQueriesGetLanguagesLanguageVm,
)
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/languages".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        'follow_redirects' : True,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[List[FilterListsDirectoryApplicationQueriesGetLanguagesLanguageVm]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = FilterListsDirectoryApplicationQueriesGetLanguagesLanguageVm.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[List[FilterListsDirectoryApplicationQueriesGetLanguagesLanguageVm]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[List[FilterListsDirectoryApplicationQueriesGetLanguagesLanguageVm]]:
    """Gets the languages targeted by the FilterLists.

    Returns:
        Response[List[FilterListsDirectoryApplicationQueriesGetLanguagesLanguageVm]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
) -> Optional[List[FilterListsDirectoryApplicationQueriesGetLanguagesLanguageVm]]:
    """Gets the languages targeted by the FilterLists.

    Returns:
        Response[List[FilterListsDirectoryApplicationQueriesGetLanguagesLanguageVm]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[List[FilterListsDirectoryApplicationQueriesGetLanguagesLanguageVm]]:
    """Gets the languages targeted by the FilterLists.

    Returns:
        Response[List[FilterListsDirectoryApplicationQueriesGetLanguagesLanguageVm]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[List[FilterListsDirectoryApplicationQueriesGetLanguagesLanguageVm]]:
    """Gets the languages targeted by the FilterLists.

    Returns:
        Response[List[FilterListsDirectoryApplicationQueriesGetLanguagesLanguageVm]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
