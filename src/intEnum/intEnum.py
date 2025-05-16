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


class SomeClassInheritsEnum(enum.IntEnum):
    ALL = -1
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    # def __contains__(self, value):
    #     return value in self._value2member_map_