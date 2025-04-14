from src.dict.dict import MyClass

def test_my_class_stats() -> None:
	mc = MyClass()
	assert mc.stats[mc.STATS_0_KEY_NAME] == 0
	mc.set_stats()
	assert mc.stats[mc.STATS_0_KEY_NAME] >= -100 and mc.stats[mc.STATS_0_KEY_NAME] <= 100