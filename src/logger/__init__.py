import logging
import os
from logging.handlers import RotatingFileHandler
from from_root import from_root
from datetime import datetime

## Constant for log configuration
LOG_DIR = "logs"
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
MAX_LOG_SIZE = 5*1024*1024  # 5MB
BACKUP_COUNT = 3 # Number of backup log files to keep


## Construct log file path 
# from root find this main path 
log_dir_path = os.path.join(from_root(), LOG_DIR) ## creating log folder 
os.makedirs(log_dir_path, exist_ok=True)
log_file_path = os.path.join(log_dir_path, LOG_FILE) ## creating log file


def configure_logger():
    """
    Configures logging with rotating file handler and a console handler
    """

    ## creating logger 
    ## creating file handler and console handler
    ## adding file handler and console handler to logger

    # create a custom logger
    logger  = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Define formatter
    formatter = logging.Formatter("[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s")

    # file handler
    file_handler = RotatingFileHandler(log_file_path, maxBytes=MAX_LOG_SIZE, backupCount=3)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    # console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.DEBUG)

    # adding console handler and file handler to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


configure_logger()