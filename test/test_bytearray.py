"""
Author : sibeov
E-mail : dev@sibeov.no
"""

#
# Constants
#
DATA_RECEIVED = bytearray([0x0, 0x0, 0x0, 0xF])
DATA_EXPECTED = bytearray([0x0, 0x0, 0x0, 0xF])


#
# Tests
#
def test_value_of_bytearray() -> None:
    ba_from_dut = DATA_RECEIVED
    ba_expected = DATA_EXPECTED

    for data, data_exp in zip(ba_from_dut, ba_expected):
        assert data == data_exp, f"Octet mismatch : {data} != {data_exp}"


def test_cast_value_of_bytearray() -> None:
    ba_from_dut_rec = int.from_bytes(DATA_RECEIVED, byteorder="little")
    ba_from_dut_exp = int.from_bytes(DATA_EXPECTED, byteorder="little")

    assert (
        ba_from_dut_rec == ba_from_dut_exp
    ), f"Octet mismatch : {ba_from_dut_rec} != {ba_from_dut_exp}"
