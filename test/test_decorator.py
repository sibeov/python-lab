"""
:Author:
    sibeov
:E-mail:
    dev@sibeov.no
"""

from src.decorator.decoratoring import *


def test_single():

    @simple_dec
    def some_function():
        print("some_function : START")
        print("some_function : DONE")

    some_function()


def test_with_wrapper():

    @dec_with_wrapper
    def some_function():
        print("some_function : START")
        print("some_function : DONE")

    some_function()
