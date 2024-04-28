import logging
import os
from datetime import datetime

LOGS_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOGS_DIR, exist_ok=True)


log_filename = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
log_filepath = os.path.join(LOGS_DIR, log_filename)


logging.basicConfig(
    level=logging.INFO,
    filename=log_filepath,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)
