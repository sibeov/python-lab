"""
Author : sibeov
E-mail : dev@sibeov.no
"""

import logging
from math import log

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class SomeTestClass:
    """
    SomeTestClass is a simple class that demonstrates the use of
    dunder methods for representation and name retrieval.
    """
    def __init__(self):
        self._a = 10

    def __repr__(self):
        return f"{self.__class__.__name__}"

    # def __name__(self):
    #     return self.__class__.__name__


#
# Tests
#
def test_SomeTestClassName():
    """
    Test that the class name is SomeTestClass
    """
    stc = SomeTestClass()
    logger.debug(f"Class repr : {stc.__repr__()}")
    # logger.debug(f"Class name : {stc.__name__()}")
    logger.debug(f"Class      : {stc}")