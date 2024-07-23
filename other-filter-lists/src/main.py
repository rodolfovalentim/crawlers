from datetime import datetime
from pathlib import Path
import logging
import requests
import yaml
import sys
import time


def main(param):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }
    path_storage = '/usr/src/data/'

    eventid = datetime.now().strftime('%Y/%m/%d')  # Getting the exact time to save the logs

    with open('./src/config.yaml') as f:
        config = yaml.safe_load(f)

    logging.info('Starting cycle')
    for item in config:
        if item['interval'] == param:
            for _ in range(5):  # Maximum 5 attempts, every 10 minutes
                try:
                    logging.info(f'Request for {item["url"]}')
                    response = requests.get(item['url'], headers=headers, verify=False)
                    if response.status_code == 200:
                        Path(path_storage + eventid).mkdir(parents=True, exist_ok=True)
                        f_name = path_storage + eventid + '/' + item['name'].replace(' ', '_').replace('/', '_').lower()
                        with open(f_name, 'wb') as f:
                            f.write(response.content)
                        break  # Exit loop of attempts
                    else:
                        logging.warning(f'{item["url"]} returns code {response.status_code}')
                except Exception as e:
                    logging.error(e)
                time.sleep(600)  # Sleep for 10 minutes between attempts
    logging.info('Cycle completed')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python script.py parameter')
        sys.exit(1)
    parameter = sys.argv[1]
    main(parameter)
