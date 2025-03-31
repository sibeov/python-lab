# Imports
import asyncio
from asyncio import taskgroups
import subprocess as sp

# Classes
class QuartusVersionError(ValueError):
	def __init__(self, message_:str):
		self._message = message_
		super().__init__(self._message)

	def __str__(self):
		return self._message

# Methods
async def get_quartus_map_version() -> sp.CompletedProcess:
	call = ["quartus_map", "--version"]
	return sp.run(call, capture_output=True, text=True)

async def get_quartus_map_version_from_result(version_string_:str) -> str:
	version = "-1"
	lower_strings = [t.lower() for t in version_string_.split()]
	if "version" in lower_strings:
		version_string_index = lower_strings.index("version")
		version = lower_strings[version_string_index + 1]

	return version

def check_version(version_string_:str, required_version_:str = "18.1.1") -> None:
	if not version_string_ == required_version_:
		raise QuartusVersionError(f"Quartus Version {version_string_} does not match required version {required_version_}")

async def main() -> int:
	version = "-1"
	async with asyncio.TaskGroup() as task_group:
		t1 = task_group.create_task(get_quartus_map_version())
		t1_results = await t1
		t2 = task_group.create_task(get_quartus_map_version_from_result(t1_results.stdout))
		t2_results = await t2

	try:
		check_version(t2_results, "18.1.1")
	except:
		raise Exception("Quartus not installed or version is not 18.1.1!")

	return 0