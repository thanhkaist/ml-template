"""Main script."""

import logging

from my_package import util


def main():
    """Main function."""

    config = util.get_config_from_yaml_with_arg("My Python Demo")

    if "logger" in config.keys():
        log_file = config["logger"].get("log_file", "log/test.log")
        logger = util.get_logger(log_file, logging.WARNING)
    else:
        logger = util.get_logger("log/test.log", logging.WARNING)

    # Example log message
    logger.debug("This is a debug message")
    logger.info("Logging to both file and terminal!")
    logger.warning("You have been warned!")
    logger.error("An error occurred")
    logger.critical("This is a critical message")


if __name__ == "__main__":
    main()
