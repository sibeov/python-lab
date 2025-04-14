from pathlib import Path
from itertools import product
from math import log

from . import get_logger

logger = get_logger(Path(__file__).name)


def test_itertools_product_basic() -> None:
    possible_values = {
        "k1": [1, 2, 3, 4],
        "k2": [False, True],
        "k3": ["Hello", "World", "Nope!"],
    }
    keys = list(possible_values.keys())
    values = list(possible_values.values())

    possible_combinations = product(*values)

    result = [dict(zip(keys, combination)) for combination in possible_combinations]
    for e in result:
        print(e)
