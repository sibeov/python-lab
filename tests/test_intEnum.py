"""
Author: DE/sbo
"""

# Imports
from src.intEnum.intEnum import SomeEnum, SomeOtherEnum

def test_is_in_SomeEnum():
	assert -1 in SomeEnum, "-1 shall be in structure"
	assert 0 in SomeEnum, "0 shall be in structure"
	assert 1 in SomeEnum, "1 shall be in structure"
	assert 2 not in SomeEnum, "2 shall NOT be in structure"

def test_SomeOtherEnum():
	assert SomeOtherEnum.VALUE_3 == 3