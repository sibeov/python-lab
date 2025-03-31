"""
Author: DE/sbo
"""

import random

import logging
logger = logging.getLogger(__file__)

from src.case.case import check_int_enum, check_string_enum

def test_string_case():
	assert check_string_enum("test_1") == True
	assert check_string_enum("test_2") == True
	assert check_string_enum("test_3") == True
	assert check_string_enum("test_4") == True
	assert check_string_enum("test_5") == False
	assert check_string_enum("TEST_1") == False
	assert check_string_enum("TEST_2") == False
	assert check_string_enum("TEST_3") == False
	assert check_string_enum("TEST_4") == False

def test_int_case():
	random_number_span = 20000
	lower_bound = int((-1) * (random_number_span / 2))
	upper_bound = int(random_number_span / 2)

	number_of_random_samples = 200
	random_numbers = random.sample(range(lower_bound, upper_bound, 1), number_of_random_samples)

	for num in random_numbers:
		if (num >= 0) and (num <= 4):
			assert check_int_enum(num) == True
		else:
			assert check_int_enum(num) == False