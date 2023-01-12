from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="FilterListsDirectoryApiContractsModelsListVm")


@attr.s(auto_attribs=True)
class FilterListsDirectoryApiContractsModelsListVm:
    """
    Attributes:
        id (Union[Unset, int]): The identifier. Example: 301.
        name (Union[Unset, str]): The unique name in title case. Example: EasyList.
        description (Union[Unset, None, str]): The brief description in English (preferably quoted from the project).
            Example: EasyList is the primary filter list that removes most adverts from international web pages, including
            unwanted frames, images, and objects. It is the most popular list used by many ad blockers and forms the basis
            of over a dozen combination and supplementary filter lists..
        license_id (Union[Unset, int]): The identifier of the License under which this FilterList is released. Example:
            4.
        syntax_ids (Union[Unset, List[int]]): The identifiers of the Syntaxes implemented by this FilterList. Example:
            [3].
        language_ids (Union[Unset, List[int]]): The identifiers of the Languages targeted by this FilterList. Example:
            [37].
        tag_ids (Union[Unset, List[int]]): The identifiers of the Tags applied to this FilterList. Example: [2].
        primary_view_url (Union[Unset, None, str]): The primary view URL. Example:
            https://easylist.to/easylist/easylist.txt.
        maintainer_ids (Union[Unset, List[int]]): The identifiers of the Maintainers of this FilterList. Example: [7].
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    license_id: Union[Unset, int] = UNSET
    syntax_ids: Union[Unset, List[int]] = UNSET
    language_ids: Union[Unset, List[int]] = UNSET
    tag_ids: Union[Unset, List[int]] = UNSET
    primary_view_url: Union[Unset, None, str] = UNSET
    maintainer_ids: Union[Unset, List[int]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        description = self.description
        license_id = self.license_id
        syntax_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.syntax_ids, Unset):
            syntax_ids = self.syntax_ids

        language_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.language_ids, Unset):
            language_ids = self.language_ids

        tag_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.tag_ids, Unset):
            tag_ids = self.tag_ids

        primary_view_url = self.primary_view_url
        maintainer_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.maintainer_ids, Unset):
            maintainer_ids = self.maintainer_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if license_id is not UNSET:
            field_dict["licenseId"] = license_id
        if syntax_ids is not UNSET:
            field_dict["syntaxIds"] = syntax_ids
        if language_ids is not UNSET:
            field_dict["languageIds"] = language_ids
        if tag_ids is not UNSET:
            field_dict["tagIds"] = tag_ids
        if primary_view_url is not UNSET:
            field_dict["primaryViewUrl"] = primary_view_url
        if maintainer_ids is not UNSET:
            field_dict["maintainerIds"] = maintainer_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        license_id = d.pop("licenseId", UNSET)

        syntax_ids = cast(List[int], d.pop("syntaxIds", UNSET))

        language_ids = cast(List[int], d.pop("languageIds", UNSET))

        tag_ids = cast(List[int], d.pop("tagIds", UNSET))

        primary_view_url = d.pop("primaryViewUrl", UNSET)

        maintainer_ids = cast(List[int], d.pop("maintainerIds", UNSET))

        filter_lists_directory_api_contracts_models_list_vm = cls(
            id=id,
            name=name,
            description=description,
            license_id=license_id,
            syntax_ids=syntax_ids,
            language_ids=language_ids,
            tag_ids=tag_ids,
            primary_view_url=primary_view_url,
            maintainer_ids=maintainer_ids,
        )

        return filter_lists_directory_api_contracts_models_list_vm
