import pytest
from seasons import calculate_mins


def test_valid_input():
    assert (
        calculate_mins("1990-11-20")
        == "Seventeen million, nine hundred fifty-two thousand, four hundred eighty minutes"
    )


def test_invalid_input():
    with pytest.raises(SystemExit):
        calculate_mins("cat") == "Invalid date"
    with pytest.raises(SystemExit):
        calculate_mins("1990-20-11") == "Invalid date"
