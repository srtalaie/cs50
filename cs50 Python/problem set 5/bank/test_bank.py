from bank import value


def test_zero():
    assert value("Hello, New_Man") == 0


def test_twenty():
    assert value("How you doing?") == 20


def test_hundred():
    assert value("What's happening?") == 100


def test_case_insensitivity():
    assert value("HeLLo, New_Man") == 0
    assert value("HOW IS IT GOING?") == 20
    assert value("wHat'S HaPPeniNg?") == 100


def test_incorrect_values():
    assert value("Hello, Newman") != 20
    assert value("Hello, Newman") != 100
    assert value("Henlo, Newman") != 0
    assert value("Henlo, Newman") != 100
    assert value("What up, Newman") != 0
    assert value("What up, Newman") != 20
