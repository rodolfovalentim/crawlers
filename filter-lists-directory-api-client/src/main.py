from filter_lists_directory_api_client import Client
from filter_lists_directory_api_client.models import filter_lists_directory_api_contracts_models_list_details_vm
from filter_lists_directory_api_client.api.lists import get_lists
from filter_lists_directory_api_client.api.languages import get_languages
from filter_lists_directory_api_client.api.tags import get_tags
from filter_lists_directory_api_client.api.syntaxes import get_syntaxes
from filter_lists_directory_api_client.api.lists import get_lists_id
from filter_lists_directory_api_client.api.tags import get_tags

from filter_lists_directory_api_client.types import Response
import requests
from datetime import datetime
from pathlib import Path
import logging
import json

from requests.exceptions import Timeout, RequestException


def get_only_interesting_tags(meta, syntax_dict, language_dict, tag_dict):
    list_modified_meta = {}
    list_modified_meta['id'] = meta.get('id')
    list_modified_meta['name'] = meta.get('name')
    list_modified_meta['syntaxes'] = [ syntax_dict[id] for id in meta.get('syntaxIds', []) ]
    list_modified_meta['languages'] = [ language_dict[id] for id in meta.get('languageIds', []) ]
    list_modified_meta['tags'] = [ tag_dict[id] for id in meta.get('tagIds', []) ]
    list_modified_meta['viewUrls'] = meta.get('viewUrls')

    return list_modified_meta

path_storage = '/usr/src/data/'

client = Client(base_url="https://filterlists.com/api/directory", verify_ssl=False)

# getting the exact time to save the logs
eventid = datetime.now().strftime("%Y/%m/%d")

# Loading a mapping from id to systax. 
syntaxes = get_syntaxes.sync(client=client)
print(syntaxes)
syntax_dict = { syntax.id: syntax.name for syntax in syntaxes }

# Loading a mapping from id to language. 
languages = get_languages.sync(client=client)
language_dict = { language.id: language.name for language in languages }

# Loading a mapping from id to tag
tags = get_tags.sync(client=client)
tag_dict = { tag.id: tag.name for tag in tags }

# get all lists
lists = get_lists.sync(client=client)

# Retry timeouts in seconds
timeouts = [5, 10, 20]

for list in lists:
    try:
        list_meta = get_lists_id.sync(id=list.id, client=client)
        list_meta_dict = list_meta.to_dict()
        list_modified_meta = get_only_interesting_tags(list_meta_dict, syntax_dict=syntax_dict, language_dict=language_dict, tag_dict=tag_dict)
        
        # Retry mechanism for requests.get
        list_content = None
        for timeout in timeouts:
            try:
                list_content = requests.get(list.primary_view_url, timeout=timeout)
                list_content.raise_for_status()  # Ensure we catch HTTP errors
                break  # Exit loop if successful
            except Timeout:
                logging.warning(f"Timeout after {timeout} seconds for URL: {list.primary_view_url}")
            except RequestException as e:
                logging.error(f"Request failed for URL: {list.primary_view_url} with error: {e}")
                break  # Exit loop on non-timeout related errors

        if list_content is None:
            raise Exception(f"Failed to retrieve content after multiple attempts for URL: {list.primary_view_url}")

        for tag_id in list_meta.tag_ids:
            tag_name = tag_dict[tag_id]
            save_path = Path(f"{path_storage}{eventid}/{tag_name}/{list_meta.name}")
            save_path.mkdir(parents=True, exist_ok=True)

            with open(save_path / 'data.txt', 'wb') as f:
                f.write(list_content.content)

            with open(save_path / 'meta.json', 'w', encoding='utf-8') as fp:
                json.dump(list_modified_meta, fp, ensure_ascii=False, indent=4)

    except Exception as e:
        logging.error(f"Error processing list {list.id}: {e}")

