""" This script demonstrates how to log to a file and terminal """

import logging
import os


def get_logger(log_file, log_level=logging.INFO):
    """Return a logger with file and terminal handlers.

    - File handler logs all messages (DEBUG and above).
    - Terminal handler logs messages at the specified log level and above.
    """
    logger = logging.getLogger("logger")

    logger.setLevel(logging.DEBUG)

    # Prevent duplicate handlers
    if logger.hasHandlers():
        logger.handlers.clear()

    # Check if log_file folder exists
    if os.path.dirname(log_file) and not os.path.exists(os.path.dirname(log_file)):
        os.makedirs(os.path.dirname(log_file))

    # Create a file handler
    file_handler = logging.FileHandler(log_file, mode="w")  # Overwrite file each run
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    )

    # log all messages with file handler
    file_handler.setLevel(logging.DEBUG)

    # Create a stream handler (console)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    )
    console_handler.setLevel(log_level)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


if __name__ == "__main__":
    # Get logger
    logger = get_logger("log/test.log", logging.WARNING)
    # Example log message
    logger.debug("This is a debug message")
    logger.info("Logging to both file and terminal!")
    logger.warning("You have been warned!")
    logger.error("An error occurred")
    logger.critical("This is a critical message")
