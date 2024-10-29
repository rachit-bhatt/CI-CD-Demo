# tests/test_main.py
import pytest
from main import calculate_area

@pytest.mark.parametrize("length, width, expected", [
    (5, 10, 50),      # Normal case
    (0, 10, 0),       # Edge case with zero
    (5, 0, 0),        # Another edge case with zero
    (3, 7, 21)        # Another normal case
])
def test_calculate_area(length, width, expected):
    assert calculate_area(length, width) == expected

def test_calculate_area_negative():
    # Testing for ValueError on negative input
    with pytest.raises(ValueError):
        calculate_area(-5, 10)