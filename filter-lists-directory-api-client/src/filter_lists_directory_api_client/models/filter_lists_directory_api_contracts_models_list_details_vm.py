from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.filter_lists_directory_api_contracts_models_list_details_vm_view_url_vm import (
    FilterListsDirectoryApiContractsModelsListDetailsVmViewUrlVm,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="FilterListsDirectoryApiContractsModelsListDetailsVm")


@attr.s(auto_attribs=True)
class FilterListsDirectoryApiContractsModelsListDetailsVm:
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
        view_urls (Union[Unset, List[FilterListsDirectoryApiContractsModelsListDetailsVmViewUrlVm]]): The view URLs.
        home_url (Union[Unset, None, str]): The URL of the home page. Example: https://easylist.to/.
        onion_url (Union[Unset, None, str]): The URL of the Tor / Onion page.
        policy_url (Union[Unset, None, str]): The URL of the policy/guidelines for the types of rules this FilterList
            includes.
        submission_url (Union[Unset, None, str]): The URL of the submission/contact form for adding rules to this
            FilterList.
        issues_url (Union[Unset, None, str]): The URL of the GitHub Issues page. Example:
            https://github.com/easylist/easylist/issues.
        forum_url (Union[Unset, None, str]): The URL of the forum page. Example:
            https://forums.lanik.us/viewforum.php?f=23.
        chat_url (Union[Unset, None, str]): The URL of the chat room.
        email_address (Union[Unset, None, str]): The email address at which the project can be contacted. Example:
            easylist@protonmail.com.
        donate_url (Union[Unset, None, str]): The URL at which donations to the project can be made.
        maintainer_ids (Union[Unset, List[int]]): The identifiers of the Maintainers of this FilterList. Example: [7].
        upstream_filter_list_ids (Union[Unset, List[int]]): The identifiers of the FilterLists from which this
            FilterList was forked.
        fork_filter_list_ids (Union[Unset, List[int]]): The identifiers of the FilterLists that have been forked from
            this FilterList. Example: [166, 565].
        included_in_filter_list_ids (Union[Unset, List[int]]): The identifiers of the FilterLists that include this
            FilterList.
        includes_filter_list_ids (Union[Unset, List[int]]): The identifiers of the FilterLists that this FilterList
            includes. Example: [11, 13, 168].
        dependency_filter_list_ids (Union[Unset, List[int]]): The identifiers of the FilterLists that this FilterList
            depends upon.
        dependent_filter_list_ids (Union[Unset, List[int]]): The identifiers of the FilterLists dependent upon this
            FilterList.
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    license_id: Union[Unset, int] = UNSET
    syntax_ids: Union[Unset, List[int]] = UNSET
    language_ids: Union[Unset, List[int]] = UNSET
    tag_ids: Union[Unset, List[int]] = UNSET
    view_urls: Union[Unset, List[FilterListsDirectoryApiContractsModelsListDetailsVmViewUrlVm]] = UNSET
    home_url: Union[Unset, None, str] = UNSET
    onion_url: Union[Unset, None, str] = UNSET
    policy_url: Union[Unset, None, str] = UNSET
    submission_url: Union[Unset, None, str] = UNSET
    issues_url: Union[Unset, None, str] = UNSET
    forum_url: Union[Unset, None, str] = UNSET
    chat_url: Union[Unset, None, str] = UNSET
    email_address: Union[Unset, None, str] = UNSET
    donate_url: Union[Unset, None, str] = UNSET
    maintainer_ids: Union[Unset, List[int]] = UNSET
    upstream_filter_list_ids: Union[Unset, List[int]] = UNSET
    fork_filter_list_ids: Union[Unset, List[int]] = UNSET
    included_in_filter_list_ids: Union[Unset, List[int]] = UNSET
    includes_filter_list_ids: Union[Unset, List[int]] = UNSET
    dependency_filter_list_ids: Union[Unset, List[int]] = UNSET
    dependent_filter_list_ids: Union[Unset, List[int]] = UNSET

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

        view_urls: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.view_urls, Unset):
            view_urls = []
            for view_urls_item_data in self.view_urls:
                view_urls_item = view_urls_item_data.to_dict()

                view_urls.append(view_urls_item)

        home_url = self.home_url
        onion_url = self.onion_url
        policy_url = self.policy_url
        submission_url = self.submission_url
        issues_url = self.issues_url
        forum_url = self.forum_url
        chat_url = self.chat_url
        email_address = self.email_address
        donate_url = self.donate_url
        maintainer_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.maintainer_ids, Unset):
            maintainer_ids = self.maintainer_ids

        upstream_filter_list_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.upstream_filter_list_ids, Unset):
            upstream_filter_list_ids = self.upstream_filter_list_ids

        fork_filter_list_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.fork_filter_list_ids, Unset):
            fork_filter_list_ids = self.fork_filter_list_ids

        included_in_filter_list_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.included_in_filter_list_ids, Unset):
            included_in_filter_list_ids = self.included_in_filter_list_ids

        includes_filter_list_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.includes_filter_list_ids, Unset):
            includes_filter_list_ids = self.includes_filter_list_ids

        dependency_filter_list_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.dependency_filter_list_ids, Unset):
            dependency_filter_list_ids = self.dependency_filter_list_ids

        dependent_filter_list_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.dependent_filter_list_ids, Unset):
            dependent_filter_list_ids = self.dependent_filter_list_ids

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
        if view_urls is not UNSET:
            field_dict["viewUrls"] = view_urls
        if home_url is not UNSET:
            field_dict["homeUrl"] = home_url
        if onion_url is not UNSET:
            field_dict["onionUrl"] = onion_url
        if policy_url is not UNSET:
            field_dict["policyUrl"] = policy_url
        if submission_url is not UNSET:
            field_dict["submissionUrl"] = submission_url
        if issues_url is not UNSET:
            field_dict["issuesUrl"] = issues_url
        if forum_url is not UNSET:
            field_dict["forumUrl"] = forum_url
        if chat_url is not UNSET:
            field_dict["chatUrl"] = chat_url
        if email_address is not UNSET:
            field_dict["emailAddress"] = email_address
        if donate_url is not UNSET:
            field_dict["donateUrl"] = donate_url
        if maintainer_ids is not UNSET:
            field_dict["maintainerIds"] = maintainer_ids
        if upstream_filter_list_ids is not UNSET:
            field_dict["upstreamFilterListIds"] = upstream_filter_list_ids
        if fork_filter_list_ids is not UNSET:
            field_dict["forkFilterListIds"] = fork_filter_list_ids
        if included_in_filter_list_ids is not UNSET:
            field_dict["includedInFilterListIds"] = included_in_filter_list_ids
        if includes_filter_list_ids is not UNSET:
            field_dict["includesFilterListIds"] = includes_filter_list_ids
        if dependency_filter_list_ids is not UNSET:
            field_dict["dependencyFilterListIds"] = dependency_filter_list_ids
        if dependent_filter_list_ids is not UNSET:
            field_dict["dependentFilterListIds"] = dependent_filter_list_ids

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

        view_urls = []
        _view_urls = d.pop("viewUrls", UNSET)
        for view_urls_item_data in _view_urls or []:
            view_urls_item = FilterListsDirectoryApiContractsModelsListDetailsVmViewUrlVm.from_dict(view_urls_item_data)

            view_urls.append(view_urls_item)

        home_url = d.pop("homeUrl", UNSET)

        onion_url = d.pop("onionUrl", UNSET)

        policy_url = d.pop("policyUrl", UNSET)

        submission_url = d.pop("submissionUrl", UNSET)

        issues_url = d.pop("issuesUrl", UNSET)

        forum_url = d.pop("forumUrl", UNSET)

        chat_url = d.pop("chatUrl", UNSET)

        email_address = d.pop("emailAddress", UNSET)

        donate_url = d.pop("donateUrl", UNSET)

        maintainer_ids = cast(List[int], d.pop("maintainerIds", UNSET))

        upstream_filter_list_ids = cast(List[int], d.pop("upstreamFilterListIds", UNSET))

        fork_filter_list_ids = cast(List[int], d.pop("forkFilterListIds", UNSET))

        included_in_filter_list_ids = cast(List[int], d.pop("includedInFilterListIds", UNSET))

        includes_filter_list_ids = cast(List[int], d.pop("includesFilterListIds", UNSET))

        dependency_filter_list_ids = cast(List[int], d.pop("dependencyFilterListIds", UNSET))

        dependent_filter_list_ids = cast(List[int], d.pop("dependentFilterListIds", UNSET))

        filter_lists_directory_api_contracts_models_list_details_vm = cls(
            id=id,
            name=name,
            description=description,
            license_id=license_id,
            syntax_ids=syntax_ids,
            language_ids=language_ids,
            tag_ids=tag_ids,
            view_urls=view_urls,
            home_url=home_url,
            onion_url=onion_url,
            policy_url=policy_url,
            submission_url=submission_url,
            issues_url=issues_url,
            forum_url=forum_url,
            chat_url=chat_url,
            email_address=email_address,
            donate_url=donate_url,
            maintainer_ids=maintainer_ids,
            upstream_filter_list_ids=upstream_filter_list_ids,
            fork_filter_list_ids=fork_filter_list_ids,
            included_in_filter_list_ids=included_in_filter_list_ids,
            includes_filter_list_ids=includes_filter_list_ids,
            dependency_filter_list_ids=dependency_filter_list_ids,
            dependent_filter_list_ids=dependent_filter_list_ids,
        )

        return filter_lists_directory_api_contracts_models_list_details_vm
