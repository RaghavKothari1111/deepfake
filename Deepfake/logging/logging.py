import logging
import os 
import datetime

LOG_FILE=f"{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.log"

logs_path=os.path.join(os.getcwd(), "logging")

if not os.path.exists(logs_path):
    os.makedirs(logs_path)

LOG_FILE_PATH=os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)



