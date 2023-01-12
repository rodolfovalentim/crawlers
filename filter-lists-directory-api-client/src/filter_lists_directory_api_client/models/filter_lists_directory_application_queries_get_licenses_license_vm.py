from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="FilterListsDirectoryApplicationQueriesGetLicensesLicenseVm")


@attr.s(auto_attribs=True)
class FilterListsDirectoryApplicationQueriesGetLicensesLicenseVm:
    """
    Attributes:
        id (Union[Unset, int]): The identifier. Example: 5.
        name (Union[Unset, str]): The unique name. Example: All Rights Reserved.
        url (Union[Unset, None, str]): The URL of the home page. Example:
            https://en.wikipedia.org/wiki/All_rights_reserved.
        permits_modification (Union[Unset, bool]): If the License permits modification.
        permits_distribution (Union[Unset, bool]): If the License permits distribution.
        permits_commercial_use (Union[Unset, bool]): If the License permits commercial use.
        filter_list_ids (Union[Unset, List[int]]): The identifiers of the FilterLists released under this License.
            Example: [6, 31].
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    url: Union[Unset, None, str] = UNSET
    permits_modification: Union[Unset, bool] = UNSET
    permits_distribution: Union[Unset, bool] = UNSET
    permits_commercial_use: Union[Unset, bool] = UNSET
    filter_list_ids: Union[Unset, List[int]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        url = self.url
        permits_modification = self.permits_modification
        permits_distribution = self.permits_distribution
        permits_commercial_use = self.permits_commercial_use
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
        if permits_modification is not UNSET:
            field_dict["permitsModification"] = permits_modification
        if permits_distribution is not UNSET:
            field_dict["permitsDistribution"] = permits_distribution
        if permits_commercial_use is not UNSET:
            field_dict["permitsCommercialUse"] = permits_commercial_use
        if filter_list_ids is not UNSET:
            field_dict["filterListIds"] = filter_list_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        url = d.pop("url", UNSET)

        permits_modification = d.pop("permitsModification", UNSET)

        permits_distribution = d.pop("permitsDistribution", UNSET)

        permits_commercial_use = d.pop("permitsCommercialUse", UNSET)

        filter_list_ids = cast(List[int], d.pop("filterListIds", UNSET))

        filter_lists_directory_application_queries_get_licenses_license_vm = cls(
            id=id,
            name=name,
            url=url,
            permits_modification=permits_modification,
            permits_distribution=permits_distribution,
            permits_commercial_use=permits_commercial_use,
            filter_list_ids=filter_list_ids,
        )

        return filter_lists_directory_application_queries_get_licenses_license_vm
