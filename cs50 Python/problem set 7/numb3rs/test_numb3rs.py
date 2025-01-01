from numb3rs import validate


def test_valid_ip():
    assert validate("255.255.255.255") == True


def test_invalid_ip():
    assert validate("512.512.512.512") == False
    assert validate("75.456.76.65") == False
    assert validate("1.2.3.1000") == False


def test_incomplete_ip():
    assert validate("255.") == False


def test_invalid_string():
    assert validate("cs50") == False
