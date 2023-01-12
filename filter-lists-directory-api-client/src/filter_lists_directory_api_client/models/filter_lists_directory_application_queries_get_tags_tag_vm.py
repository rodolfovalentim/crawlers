from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="FilterListsDirectoryApplicationQueriesGetTagsTagVm")


@attr.s(auto_attribs=True)
class FilterListsDirectoryApplicationQueriesGetTagsTagVm:
    """
    Attributes:
        id (Union[Unset, int]): The identifier. Example: 2.
        name (Union[Unset, str]): The unique name. Example: ads.
        description (Union[Unset, None, str]): The description. Example: Blocks advertisements.
        filter_list_ids (Union[Unset, List[int]]): The identifiers of the FilterLists to which this Tag is applied.
            Example: [1, 3, 6].
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    filter_list_ids: Union[Unset, List[int]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        description = self.description
        filter_list_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.filter_list_ids, Unset):
            filter_list_ids = self.filter_list_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if filter_list_ids is not UNSET:
            field_dict["filterListIds"] = filter_list_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        filter_list_ids = cast(List[int], d.pop("filterListIds", UNSET))

        filter_lists_directory_application_queries_get_tags_tag_vm = cls(
            id=id,
            name=name,
            description=description,
            filter_list_ids=filter_list_ids,
        )

        return filter_lists_directory_application_queries_get_tags_tag_vm
