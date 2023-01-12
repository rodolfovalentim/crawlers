from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="FilterListsDirectoryApiContractsModelsListDetailsVmViewUrlVm")


@attr.s(auto_attribs=True)
class FilterListsDirectoryApiContractsModelsListDetailsVmViewUrlVm:
    """
    Attributes:
        segment_number (Union[Unset, int]): The segment number of the URL for the FilterList (for multi-part lists).
            Example: 1.
        primariness (Union[Unset, int]): How primary the URL is for the FilterList segment (1 is original, 2+ is a
            mirror; unique per SegmentNumber) Example: 1.
        url (Union[Unset, str]): The view URL. Example: https://easylist.to/easylist/easylist.txt.
    """

    segment_number: Union[Unset, int] = UNSET
    primariness: Union[Unset, int] = UNSET
    url: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        segment_number = self.segment_number
        primariness = self.primariness
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if segment_number is not UNSET:
            field_dict["segmentNumber"] = segment_number
        if primariness is not UNSET:
            field_dict["primariness"] = primariness
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        segment_number = d.pop("segmentNumber", UNSET)

        primariness = d.pop("primariness", UNSET)

        url = d.pop("url", UNSET)

        filter_lists_directory_api_contracts_models_list_details_vm_view_url_vm = cls(
            segment_number=segment_number,
            primariness=primariness,
            url=url,
        )

        return filter_lists_directory_api_contracts_models_list_details_vm_view_url_vm
