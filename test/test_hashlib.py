from hashlib import sha256

from pathlib import Path

from . import get_logger

logger = get_logger(Path(__file__).name)


def test_dut_name_to_sha256() -> None:
    dut = "test"
    logger.debug(f"Generating from {dut}")
    enc_str = dut.encode("utf-8")
    hash_of_dut = sha256(enc_str).hexdigest()
    logger.debug(f"SHA256 of {dut} = {hash_of_dut[0:4]}")
