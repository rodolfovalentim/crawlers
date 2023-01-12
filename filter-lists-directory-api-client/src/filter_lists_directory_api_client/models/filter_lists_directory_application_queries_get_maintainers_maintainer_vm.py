from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="FilterListsDirectoryApplicationQueriesGetMaintainersMaintainerVm")


@attr.s(auto_attribs=True)
class FilterListsDirectoryApplicationQueriesGetMaintainersMaintainerVm:
    """
    Attributes:
        id (Union[Unset, int]): The identifier. Example: 7.
        name (Union[Unset, str]): The unique name. Example: The EasyList Authors.
        url (Union[Unset, None, str]): The URL of the home page. Example: https://easylist.to/.
        email_address (Union[Unset, None, str]): The email address.
        twitter_handle (Union[Unset, None, str]): The Twitter handle.
        filter_list_ids (Union[Unset, List[int]]): The identifiers of the FilterLists maintained by this Maintainer.
            Example: [11, 13, 301].
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    url: Union[Unset, None, str] = UNSET
    email_address: Union[Unset, None, str] = UNSET
    twitter_handle: Union[Unset, None, str] = UNSET
    filter_list_ids: Union[Unset, List[int]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        url = self.url
        email_address = self.email_address
        twitter_handle = self.twitter_handle
        filter_list_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.filter_list_ids, Unset):
            filter_list_ids = self.filter_list_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url
        if email_address is not UNSET:
            field_dict["emailAddress"] = email_address
        if twitter_handle is not UNSET:
            field_dict["twitterHandle"] = twitter_handle
        if filter_list_ids is not UNSET:
            field_dict["filterListIds"] = filter_list_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        url = d.pop("url", UNSET)

        email_address = d.pop("emailAddress", UNSET)

        twitter_handle = d.pop("twitterHandle", UNSET)

        filter_list_ids = cast(List[int], d.pop("filterListIds", UNSET))

        filter_lists_directory_application_queries_get_maintainers_maintainer_vm = cls(
            id=id,
            name=name,
            url=url,
            email_address=email_address,
            twitter_handle=twitter_handle,
            filter_list_ids=filter_list_ids,
        )

        return filter_lists_directory_application_queries_get_maintainers_maintainer_vm
