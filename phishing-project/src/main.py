from datetime import datetime
from pathlib import Path
import logging
import requests
import yaml

path_storage = '/usr/src/data/'

# getting the exact time to save the logs
eventid = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

with open('./src/config.yaml') as f:
    config = yaml.safe_load(f)

for filename in config['files']:
    try:
        list_content = requests.get(config['url'] + '/' + filename)
        Path(path_storage + eventid).mkdir(parents=True, exist_ok=True)

        with open(path_storage + eventid + '/' + filename, 'wb') as f:
            f.write(list_content.content)

    except Exception as ecpt:
        logging.error(ecpt)
    
    exit
