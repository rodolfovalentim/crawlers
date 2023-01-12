from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="FilterListsDirectoryApplicationQueriesGetSyntaxesSyntaxVm")


@attr.s(auto_attribs=True)
class FilterListsDirectoryApplicationQueriesGetSyntaxesSyntaxVm:
    """
    Attributes:
        id (Union[Unset, int]): The identifier. Example: 3.
        name (Union[Unset, str]): The unique name. Example: Adblock Plus.
        description (Union[Unset, None, str]): The description.
        url (Union[Unset, None, str]): The URL of the home page. Example: https://adblockplus.org/filters.
        filter_list_ids (Union[Unset, List[int]]): The identifiers of the FilterLists implementing this Syntax. Example:
            [2, 6, 11].
        software_ids (Union[Unset, List[int]]): The identifiers of the Software that supports this Syntax. Example: [1,
            2, 3].
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    url: Union[Unset, None, str] = UNSET
    filter_list_ids: Union[Unset, List[int]] = UNSET
    software_ids: Union[Unset, List[int]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        description = self.description
        url = self.url
        filter_list_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.filter_list_ids, Unset):
            filter_list_ids = self.filter_list_ids

        software_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.software_ids, Unset):
            software_ids = self.software_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if url is not UNSET:
            field_dict["url"] = url
        if filter_list_ids is not UNSET:
            field_dict["filterListIds"] = filter_list_ids
        if software_ids is not UNSET:
            field_dict["softwareIds"] = software_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        url = d.pop("url", UNSET)

        filter_list_ids = cast(List[int], d.pop("filterListIds", UNSET))

        software_ids = cast(List[int], d.pop("softwareIds", UNSET))

        filter_lists_directory_application_queries_get_syntaxes_syntax_vm = cls(
            id=id,
            name=name,
            description=description,
            url=url,
            filter_list_ids=filter_list_ids,
            software_ids=software_ids,
        )

        return filter_lists_directory_application_queries_get_syntaxes_syntax_vm
