from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="FilterListsDirectoryApplicationQueriesGetLanguagesLanguageVm")


@attr.s(auto_attribs=True)
class FilterListsDirectoryApplicationQueriesGetLanguagesLanguageVm:
    """
    Attributes:
        id (Union[Unset, int]): The identifier. Example: 37.
        iso6391 (Union[Unset, str]): The unique ISO 639-1 code. Example: en.
        name (Union[Unset, str]): The unique ISO name. Example: English.
        filter_list_ids (Union[Unset, List[int]]): The identifiers of the FilterLists targeted by this Language.
            Example: [114, 141].
    """

    id: Union[Unset, int] = UNSET
    iso6391: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    filter_list_ids: Union[Unset, List[int]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        iso6391 = self.iso6391
        name = self.name
        filter_list_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.filter_list_ids, Unset):
            filter_list_ids = self.filter_list_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if iso6391 is not UNSET:
            field_dict["iso6391"] = iso6391
        if name is not UNSET:
            field_dict["name"] = name
        if filter_list_ids is not UNSET:
            field_dict["filterListIds"] = filter_list_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        iso6391 = d.pop("iso6391", UNSET)

        name = d.pop("name", UNSET)

        filter_list_ids = cast(List[int], d.pop("filterListIds", UNSET))

        filter_lists_directory_application_queries_get_languages_language_vm = cls(
            id=id,
            iso6391=iso6391,
            name=name,
            filter_list_ids=filter_list_ids,
        )

        return filter_lists_directory_application_queries_get_languages_language_vm
