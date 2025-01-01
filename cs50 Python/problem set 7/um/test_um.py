from um import count


def test_valid_inputs():
    assert count("Um, hello, um       ") == 2
    assert count("um this is so yummy, yum") == 1
    assert count("UM henlo?") == 1
