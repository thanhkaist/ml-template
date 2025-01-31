"""Test logger module"""

import logging
import os

from my_package.util.logger import get_logger


def test_get_logger():
    """Test get_logger"""
    logger = get_logger("log/test.log", logging.INFO)

    # logger is not root logger
    assert logger.name != "root"
    # logger level has to be DEBUG
    assert logger.level == logging.DEBUG
    assert logger.hasHandlers() is True
    # Has file handler and terminal handler
    assert len(logger.handlers) == 2
    # Check file handler
    assert logger.handlers[0].baseFilename == os.path.abspath("log/test.log")
    assert logger.handlers[0].level == logging.DEBUG
    # Check terminal handler
    assert logger.handlers[1].level == logging.INFO
