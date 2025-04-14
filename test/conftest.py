import pytest

import logging
from logging import Logger


#
# Fixtures
#
@pytest.fixture
def some_fixture() -> int:
    """
    This fixtrure recides in ./tests.
    """
    return 1
