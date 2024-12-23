from plates import is_valid


def test_under_two():
    assert is_valid("A") == False


def test_over_six():
    assert is_valid("AB12345") == False


def test_cant_start_with_num():
    assert is_valid("22AAAA") == False
    assert is_valid("1ABCDE") == False


def test_first_two_not_letters():
    assert is_valid("A1234") == False


def test_first_num_zero():
    assert is_valid("00ABB") == False
    assert is_valid("AB0123") == False


def test_no_special_chars():
    assert is_valid("AB.123") == False


def test_nums_cant_be_in_middle():
    assert is_valid("AAA22A") == False
    assert is_valid("AA22AA") == False
    assert is_valid("AA1A") == False


def test_valid_input():
    assert is_valid("ABCDE") == True
    assert is_valid("AAA222") == True
    assert is_valid("AAA200") == True
