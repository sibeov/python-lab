import enum
from enum import Enum, auto

import logging

logger = logging.getLogger(__file__)

@enum.unique
class StringEnum(enum.StrEnum):
	TEST_1 = auto()
	TEST_2 = auto()
	TEST_3 = auto()
	TEST_4 = auto()

@enum.unique
class IntEnum(enum.IntEnum):
	TEST_1 = 0
	TEST_2 = 1
	TEST_3 = 2
	TEST_4 = 3

def check_string_enum(input_:str) -> bool:
	match input_:
		case StringEnum.TEST_1:
			return True
		case StringEnum.TEST_2:
			return True
		case StringEnum.TEST_3:
			return True
		case StringEnum.TEST_4:
			return True
		case _:
			return False

def check_int_enum(input_:int) -> bool:
	match input_:
		case IntEnum.TEST_1:
			return True
		case IntEnum.TEST_2:
			return True
		case IntEnum.TEST_3:
			return True
		case IntEnum.TEST_4:
			return True
		case _:
			return False