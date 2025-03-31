"""
Author: DE/sbo
"""

from abc import ABC, abstractmethod
from typing import Sequence

class BaseClass(ABC):

	@abstractmethod
	def _write_to(self, reg_:int, data_:int) -> None:
		pass

	@abstractmethod
	def _read_from(self, reg_:int) -> Sequence[int]:
		pass


class SuperClass(BaseClass):
	def __init__(self) -> None:
		self._status_regs = []

	def _write_to(self, reg_:int, data_:int) -> None:
		if reg_ >= 0:
			if reg_ == 0:
				self._status_regs.insert(0, data_) 
			else:
				self._status_regs.insert(reg_ + 1, data_) 
		else:
			return

	def _read_from(self, reg_:int) -> Sequence[int]:
		if reg_ >= len(self._status_regs) or reg_ < 0:
			return -1
		else:
			return self._status_regs[reg_]

	# Public methods
	def write(self, addr_:int, data_:int) -> None:
		self._write_to(addr_, data_)

	def read(self, addr_:int) -> Sequence[int]:
		return self._read_from(addr_)