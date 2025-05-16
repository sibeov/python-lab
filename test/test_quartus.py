"""
Author: DE/sbo
"""

# Imports
import asyncio
import pytest

# Local
from src.quartus.version_test import main


@pytest.mark.xfail(reason="Quartus is not installed")
def test_quartus_version():
    asyncio.run(main(), debug=False)
