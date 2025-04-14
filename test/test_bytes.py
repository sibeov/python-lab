from pathlib import Path
from random import randbytes

from . import get_logger

logger = get_logger(Path(__file__).name)


def test_bytes_len() -> None:
    BYTE_ARRAY_LEN = 15
    logger.info(f"Setting byte len to {BYTE_ARRAY_LEN}")
    random_bytes = randbytes(BYTE_ARRAY_LEN)
    logger.info(f"Len of bytes are {len(random_bytes)}")
