import random

class MyClass:

	STATS_0_KEY_NAME = "my_val"

	def __init__(self):
		self._stats_0 = {}
		self._stats_0[self.STATS_0_KEY_NAME] = 0

	def _get_stats(self):
		return random.randint(-100, 100)

	def set_stats(self):
		stats = {}
		stats[self.STATS_0_KEY_NAME] = self._get_stats()
		self._stats_0 = stats

	@property
	def stats(self):
		return self._stats_0

	@stats.setter
	def stats(self, stats_):
		self._stats_0 = stats_
