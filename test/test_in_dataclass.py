"""
:Author: sibeov
:E-mail: dev@sibeov.no
"""

from dataclasses import dataclass, astuple


@dataclass
class DummyData:
    one: int = 1
    two: int = 2
    three: int = 3

    def __iter__(self):
        return iter(astuple(self.one, self.two, self.three))


def test_in_dataclass() -> None:
    if 1 in DummyData():
        assert True, "1 is in DummyData"
    else:
        assert False, "1 is not in DummyData"
