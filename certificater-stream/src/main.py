import logging
from logging.handlers import TimedRotatingFileHandler
import certstream
import json
import os

# get named logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
path_storage = os.environ.get("DATA_PATH",'/usr/src/data/')
url = os.environ.get("CT_URL",'wss://certstream.calidog.io/')

# create handler
handler = TimedRotatingFileHandler(filename=path_storage + 'runtime.log', when='midnight', 
                                   interval=1, backupCount=36_500, encoding='utf-8', delay=False)

logger.addHandler(handler)

def print_callback(message, context):
    if message['message_type'] == "heartbeat":
        return
    if message['message_type'] == "certificate_update":
        logger.info(json.dumps(message))

certstream.listen_for_events(print_callback, url=url)
