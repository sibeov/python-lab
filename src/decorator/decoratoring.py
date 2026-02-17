"""
:Author:
    sibeov
:E-mail:
    dev@sibeov.no
"""

from typing import Callable, Any


def simple_dec(func: Callable) -> Callable:
    print("simple_dec : START")
    return func
    # def wrapper(*args, **kwargs) -> Any:
    #     print("FUNCTION : START")
    #     return func(*args, **kwargs)
    #     print("FUNCTION : END")

    # return wrapper


def dec_with_wrapper(func: Callable) -> Callable:
    print("dec_with_wrapper : START")

    def wrapper() -> Any:
        print("wrapper : START")
        result = func()
        print("wrapper : DONE")
        return result

    return wrapper


__all__ = [
    "simple_dec",
    "dec_with_wrapper",
]
