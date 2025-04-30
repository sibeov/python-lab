from pathlib import Path
from random import randbytes
from construct import Bitwise, Struct, Bytes, BitsInteger

from . import get_logger

logger = get_logger(Path(__file__).name)

DATA1_FIELD = "data1"
DATA2_FIELD = "data2"
DATA3_FIELD = "data3"
DATA4_FIELD = "data4"
DATA5_FIELD = "data5"
DATA6_FIELD = "data6"
FLAGS_FIELD = "flags"

flag_struct = Bitwise(
    Struct(
        "flag_1" / BitsInteger(1),
        "flag_2" / BitsInteger(1),
        "flag_3" / BitsInteger(1),
        "flag_4" / BitsInteger(1),
        "flag_5" / BitsInteger(1),
        "flag_6" / BitsInteger(1),
        "flag_7" / BitsInteger(1),
        "flag_8" / BitsInteger(1),
    )
)

bit_struct = Struct(
    DATA1_FIELD / BitsInteger(4),
    DATA2_FIELD / BitsInteger(4),
    DATA3_FIELD / BitsInteger(4),
    DATA4_FIELD / BitsInteger(4),
    DATA5_FIELD / BitsInteger(4),
    DATA6_FIELD / BitsInteger(4),
    FLAGS_FIELD / flag_struct,
)


#
# IP
#
VerIHLField = Bitwise(
    Struct(
        "ver" / BitsInteger(4),
        "ihl" / BitsInteger(4),
    )
)

FlagsFragmentOffsetField = Bitwise(
    Struct(
        "flags" / BitsInteger(3),
        "offset" / BitsInteger(13),
    )
)

IPHeader = Struct(
    "verihl" / VerIHLField,
    "tos" / Bytes(1),
    "totlen" / Bytes(2),
    "id" / Bytes(2),
    "flagsoffset" / FlagsFragmentOffsetField,
    "ttl" / Bytes(1),
    "protocol" / Bytes(1),
    "cs" / Bytes(2),
    "srcaddr" / Bytes(4),
    "destaddr" / Bytes(4),
)


def test_print_struct() -> None:
    my_flags = {
        "flag_1": 1,
        "flag_2": 1,
        "flag_3": 1,
        "flag_4": 1,
        "flag_5": 1,
        "flag_6": 1,
        "flag_7": 1,
        "flag_8": 1,
    }

    my_struct_values = {
        DATA1_FIELD: 0x1,
        DATA2_FIELD: 0x1,
        DATA3_FIELD: 0x1,
        DATA4_FIELD: 0x1,
        DATA5_FIELD: 0x1,
        DATA6_FIELD: 0x1,
        FLAGS_FIELD: my_flags,
    }
    bit_struct.build_file(my_struct_values, "my_struct_values.bin")


def test_print_ipv4() -> None:
    ip_header = {
        "verihl": {"ver": 0x4, "ihl": 0x5},
        "tos": 0x0,
        "totlen": 0x20,
        "id": 0x0,
        "flagsoffset": {
            "flags": 0x4,
            "offset": 0x0,
        },
        "ttl": 0x0,
        "protocol": 1,
        "cs": randbytes(2),
        "srcaddr": randbytes(4),
        "destaddr": randbytes(4),
    }
    IPHeader.build_file(ip_header, "ip_header.bin")
    IPHeaderBytes = IPHeader.build(ip_header)
    for bytes in IPHeaderBytes:
        print(hex(bytes))


def test_use_bytes() -> None:
    logger.info("Testing bytes")
    byte = Bytes(1)
    byte.build(1)
