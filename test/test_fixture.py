""" Test pytest.fixture feature. 
Run: pytest test/test_fixture.py -v -s
"""

import pytest


@pytest.fixture
def setup_and_teardown():
    """Setup and teardown"""
    print("Setup")
    yield
    print("Teardown")


def test_setup_and_teardown(setup_and_teardown):
    """Test setup and teardown"""
    print("Test 1")


def test_setup_and_teardown2(setup_and_teardown):
    """Test setup and teardown"""
    print("Test 2")
