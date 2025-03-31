import enum
from enum import Enum

@enum.unique
class SomeEnum(enum.IntEnum):
	ALL = -1
	VALUE_0 = 0
	VALUE_1 = 1

@enum.unique
class SomeOtherEnum(enum.IntEnum):
	ALL = -1
	VALUE_0 = 0
	VALUE_1 = 1
	VALUE_3 = ALL + 4