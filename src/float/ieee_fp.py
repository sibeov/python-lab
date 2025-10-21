from abc import ABC, abstractmethod


class FPBase:
    def __init__(self):
        self.sign = 0
        self.exponent = 0
        self.mantissa = 0


class FPSP(FPBase):
    """
    Floating Point Single Precision (32-bit) representation.
    """

    NUM_OF_EXPONENT_BITS = 8
    NUM_OF_MANTISSA_BITS = 23

    def __init__(self, sign: int = 0, exponent: int = 0, mantissa: int = 0):
        self._exponent_bias = int((2**self.NUM_OF_EXPONENT_BITS - 1) / 2)
        self._exponent_masked = exponent & 0xFF
        self._mantissa_masked = mantissa & 0x7FFFFF
        super().__init__(sign, self._exponent_masked, self._mantissa_masked)


class FPDP:
    """
    Floating Point Double Precision (64-bit) representation.
    """

    NUM_OF_EXPONENT_BITS = 11
    NUM_OF_MANTISSA_BITS = 52

    def __init__(self, sign: int = 0, exponent: int = 0, mantissa: int = 0):
        self._exponent_bias = int((2**self.NUM_OF_EXPONENT_BITS - 1) / 2)
        self._exponent_masked = exponent & 0x7FF
        self._mantissa_masked = mantissa & 0xFFFFFFFFFFFFF
        super().__init__(sign, self._exponent_masked, self._mantissa_masked)
