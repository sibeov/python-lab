"""
:Author: sibeov
:E-mail: dev@sibeov.no
"""

from functools import singledispatch
from pickle import LIST
from tkinter import N

import numpy as np
from numpy.typing import NDArray

CustomType = tuple | str


def test_single_dispatch():
    DEFAULT_RESP = "default"
    FLOAT_RESP = "float"
    LIST_RESP = "list"
    NDARRAY_RESP = "NDarray"
    CUSTO_RESP = "custom"

    @singledispatch
    def func(arg: int):
        return DEFAULT_RESP

    @func.register
    def _(arg: float):
        return FLOAT_RESP

    @func.register
    def _(arg: list):
        return LIST_RESP

    @func.register
    def _(arg: np.ndarray):
        return NDARRAY_RESP

    @func.register
    def _(arg: CustomType):
        return CUSTO_RESP

    assert func(10) == DEFAULT_RESP
    assert func(3.14) == FLOAT_RESP
    assert func(["hello"]) == LIST_RESP
    assert func(np.array([1.0, 2.0])) == NDARRAY_RESP
    assert func((5, 2.71)) == CUSTO_RESP
    assert func("yep") == CUSTO_RESP
