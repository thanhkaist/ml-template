""" Test config module utilizaint pytest.fixture"""

import pytest

from my_package.util.config import load_config


@pytest.fixture
def config():
    """
    fixture is used to
    - initialize test environment
    - prepare data
    - clean up after the test

    In this case, we are using it to load the config file
    """
    return load_config("configs/config.yaml")


def test_load_config(config):
    """Test keys"""
    assert "logger" in config.keys()
    assert "data" in config.keys()


def test_load_config_log_file(config):
    """Test logger"""
    assert config["logger"]["log_file"] == "log/training.log"
