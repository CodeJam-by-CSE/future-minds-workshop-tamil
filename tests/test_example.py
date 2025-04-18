from sample.example import find_total
import pytest
def test_sum():
    assert find_total(1, 2) == 3
    assert find_total(-1, 1) == 0
    assert find_total(0, 0) == 0

def test_sum_2():
    assert find_total(1, 2) == 3
    assert find_total(-1, 1) == 0
    assert find_total(0, 0) == 0