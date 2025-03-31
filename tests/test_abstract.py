from src.abstract.abstract import SuperClass

def test_super_class() -> None:
	sc = SuperClass()
	test_values = [
		0x1000,
		0x1001,
		0x1002,
		0x1003,
	]

	addr = 0
	for i in test_values:
		addr += 1
		sc.write(addr, i)

	for i in range(len(test_values)):
		assert sc.read(i) == test_values[i], f"Values do not match. Value = {sc.read(i)}"