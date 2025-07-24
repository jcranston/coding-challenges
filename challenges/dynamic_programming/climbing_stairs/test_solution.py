from .solution import climbing_stairs


def test_climbing_stairs_example():
    assert climbing_stairs(0) == 1
    assert climbing_stairs(1) == 1
    assert climbing_stairs(2) == 2
    assert climbing_stairs(3) == 3
    assert climbing_stairs(4) == 5
    assert climbing_stairs(5) == 8
