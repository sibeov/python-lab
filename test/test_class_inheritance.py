from pathlib import Path
from . import get_logger

logger = get_logger(Path(__file__).name)


class BaseClass:
    def __init__(self, name: str | None = None):
        self._name = name if name != None else "BaseClass"

    @property
    def name(self) -> str:
        return self._name

    def __str__(self):
        return self.name


class SubClassA(BaseClass):
    def __init__(self, instance: int | None = None, **kwargs):
        super().__init__(**kwargs)

        self._instance = instance if instance != None else 0


class SubClassB(BaseClass):
    def __init__(self, id: int | None = None, **kwargs):
        super().__init__(**kwargs)

        self._id = id if id != None else 0

    @property
    def id(self) -> int:
        return self._id


class SubClassC(SubClassB):
    def __init__(self, other: str | None = None, **kwargs):
        super().__init__(**kwargs)

        self._other = other if other != None else "SubClassC"


def get_class(
    class_type, name="Test", id="TestID", instance="InstTest", other="OtherStuff"
):
    if class_type == SubClassA:
        return SubClassA(name=name)
    elif class_type == SubClassB:
        return SubClassB(name=name)
    elif class_type == SubClassC:
        return SubClassC(name=name, id=id)
    else:
        pass


def test_class_inheritance_kwargs() -> None:
    logger.info("Testing class inheritance")
    class_type = SubClassA
    obj = get_class(class_type)
    assert obj.name == "Test", "Should be Test!"
    logger.info(f"Class name is {obj}")


def test_class_inheritance_double() -> None:
    logger.info("Testing neste inheritance with kwargs")
    class_type = SubClassC
    obj = get_class(class_type)
    assert obj.name == "Test", "Should be Test!"
    assert obj.id == "TestID", "Should be TestID!"
