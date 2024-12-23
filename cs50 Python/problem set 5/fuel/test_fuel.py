import pytest
from fuel import convert, gauge


def test_convert():
    assert convert("1/2") == 50


def test_convert_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_convert_denominator_larger():
    with pytest.raises(ValueError):
        convert("2/1")


def test_gauge():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
