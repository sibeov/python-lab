"""
Author: DE/sbo
"""

# Imports
import asyncio
from asyncio import taskgroups
import subprocess as sp

# Local
from src.quartus.version_test import main

def test_quartus_version():
	asyncio.run(main(), debug=False)