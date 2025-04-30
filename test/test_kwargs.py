from pathlib import Path
from . import get_logger

logger = get_logger(Path(__file__).name)


def some_func(**kwargs) -> None:
    print("In some_func")


def test_some_func_kwargs() -> None:
    some_func(id="Test", name="SomeName")
