"""
Author : sibeov
E-mail : sbo@eidel.no
"""


# ----------------------------------------------------------------------------------------------------------------------
# Tests
# ----------------------------------------------------------------------------------------------------------------------
def test_args_and_kwargs() -> None:
    def some_func(*args, **kwargs):
        print(args)
        print(kwargs)

    some_func(my_face="This is my face")
