import pytest
from working import convert


def test_omit_to():
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")


def test_valid_inputs():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:25 AM to 5:40 PM") == "09:25 to 17:40"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("5 PM to 9 AM") == "17:00 to 09:00"
    assert convert("5:00 PM to 9:00 AM") == "17:00 to 09:00"
    assert convert("5 AM to 9:00 PM") == "05:00 to 21:00"
    assert convert("9:30 AM to 5:30 PM") == "09:30 to 17:30"


def test_invalid_mins():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5 PM")
