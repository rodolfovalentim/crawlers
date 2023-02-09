import logging
from logging.handlers import TimedRotatingFileHandler
import certstream
import json

# get named logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
path_storage = '/usr/src/data/'

# create handler
handler = TimedRotatingFileHandler(filename=path_storage + 'runtime.log', when='midnight', 
                                   interval=1, backupCount=36_500, encoding='utf-8', delay=False)
                                   
logger.addHandler(handler)

def print_callback(message, context):
    if message['message_type'] == "heartbeat":
        return

    if message['message_type'] == "certificate_update":
        logger.info(json.dumps(message))

certstream.listen_for_events(print_callback, url='wss://certstream.calidog.io/')
