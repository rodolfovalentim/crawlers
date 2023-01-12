from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="FilterListsDirectoryApplicationQueriesGetSoftwareSoftwareVm")


@attr.s(auto_attribs=True)
class FilterListsDirectoryApplicationQueriesGetSoftwareSoftwareVm:
    """
    Attributes:
        id (Union[Unset, int]): The identifier. Example: 2.
        name (Union[Unset, str]): The unique name. Example: Adblock Plus.
        description (Union[Unset, None, str]): The description. Example: Adblock Plus is a free extension that allows
            you to customize your web experience. You can block annoying ads, disable tracking and lots more. It’s available
            for all major desktop browsers and for your mobile devices..
        home_url (Union[Unset, None, str]): The URL of the home page. Example: https://adblockplus.org/.
        download_url (Union[Unset, None, str]): The URL of the Software download. Example: https://adblockplus.org/.
        supports_abp_url_scheme (Union[Unset, bool]): If the Software supports the abp: URL scheme to click-to-subscribe
            to a FilterList. Example: True.
        syntax_ids (Union[Unset, List[int]]): The identifiers of the Syntaxes that this Software supports. Example: [3,
            28, 38, 48].
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    home_url: Union[Unset, None, str] = UNSET
    download_url: Union[Unset, None, str] = UNSET
    supports_abp_url_scheme: Union[Unset, bool] = UNSET
    syntax_ids: Union[Unset, List[int]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        description = self.description
        home_url = self.home_url
        download_url = self.download_url
        supports_abp_url_scheme = self.supports_abp_url_scheme
        syntax_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.syntax_ids, Unset):
            syntax_ids = self.syntax_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if home_url is not UNSET:
            field_dict["homeUrl"] = home_url
        if download_url is not UNSET:
            field_dict["downloadUrl"] = download_url
        if supports_abp_url_scheme is not UNSET:
            field_dict["supportsAbpUrlScheme"] = supports_abp_url_scheme
        if syntax_ids is not UNSET:
            field_dict["syntaxIds"] = syntax_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        home_url = d.pop("homeUrl", UNSET)

        download_url = d.pop("downloadUrl", UNSET)

        supports_abp_url_scheme = d.pop("supportsAbpUrlScheme", UNSET)

        syntax_ids = cast(List[int], d.pop("syntaxIds", UNSET))

        filter_lists_directory_application_queries_get_software_software_vm = cls(
            id=id,
            name=name,
            description=description,
            home_url=home_url,
            download_url=download_url,
            supports_abp_url_scheme=supports_abp_url_scheme,
            syntax_ids=syntax_ids,
        )

        return filter_lists_directory_application_queries_get_software_software_vm
