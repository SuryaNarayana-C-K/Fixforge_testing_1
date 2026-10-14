import pytest

from calculator import divide, calculate_average
from shopping import apply_discount, get_item


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


def test_calculate_average():
    assert calculate_average([10, 20, 30]) == 20


def test_apply_discount():
    assert apply_discount(100, 20) == 80


def test_get_item_out_of_range():
    assert get_item([10, 20, 30], 3) is None