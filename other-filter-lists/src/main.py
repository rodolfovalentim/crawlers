from datetime import datetime
from pathlib import Path
import logging
import requests
import yaml
import sys

def main(param):

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}
    path_storage = '/usr/src/data/'

    # Getting the exact time to save the logs
    eventid = datetime.now().strftime("%Y/%m/%d")

    with open('./src/config.yaml') as f:
        config = yaml.safe_load(f)

    for item in config:
        if item['interval'] == param:
            try:
                logging.error(item['url'])
                list_content = requests.get(item['url'], headers=headers, verify=False)
                Path(path_storage + eventid).mkdir(parents=True, exist_ok=True)
                with open(path_storage + eventid + '/' + item['name'].replace(' ', '_').replace('/', '_').lower(), 'wb') as f:
                    f.write(list_content.content)

            except Exception as ecpt:
                logging.error(ecpt)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py parameter")
        sys.exit(1)
    parameter = sys.argv[1]
    main(parameter)
