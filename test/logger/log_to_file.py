""" This script demonstrates how to log to a file """

import logging

# Loggin to a file
logging.basicConfig(
    filename="test.log",
    filemode="w",
    format="%(asctime)s - %(levelname)s : %(message)s",
    level=logging.INFO,
)

logging.debug(
    "This is a debug message"
)  # This will not be printed due to the level INFO
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")
