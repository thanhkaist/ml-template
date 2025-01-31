"""Main script."""

import logging

from my_package.util.logger import get_logger


def main():
    """Main function."""
    logger = get_logger("log/test.log", logging.WARNING)

    # Example log message
    logger.debug("This is a debug message")
    logger.info("Logging to both file and terminal!")
    logger.warning("You have been warned!")
    logger.error("An error occurred")
    logger.critical("This is a critical message")


if __name__ == "__main__":
    main()
