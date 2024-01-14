import os
import sys
import logging
from datetime import datetime


LOG_FILE_NAME = f'{datetime.now().strftime("%m_%d_%Y__%H_%S")}.log'
logs_path = os.path.join(os.getcwd(),'logs')

os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
 format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
 level=logging.INFO
 )