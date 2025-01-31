""" Test logging module
"""

import logging

# configure logging
logging.basicConfig(level=logging.INFO)


# log messsages

logging.debug(
    "This is a debug message"
)  # This will not be printed due to the level INFO
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")
