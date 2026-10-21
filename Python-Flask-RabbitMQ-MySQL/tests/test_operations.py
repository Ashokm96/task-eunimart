import pytest

from app.controllers.operations import calculate_operation


def test_sum_numbers():
    assert calculate_operation("sum", [8, 4, 2]) == 14


def test_subtract_numbers():
    assert calculate_operation("subtract", [10, 3, 2]) == 5


def test_multiply_numbers():
    assert calculate_operation("multiply", [2, 3, 4]) == 24


def test_divide_numbers():
    assert calculate_operation("divide", [20, 2, 5]) == 2


def test_divide_by_zero_is_rejected():
    with pytest.raises(ZeroDivisionError, match="divide by zero"):
        calculate_operation("divide", [10, 0])


def test_unknown_operation_is_rejected():
    with pytest.raises(ValueError, match="Unsupported operation"):
        calculate_operation("modulo", [10, 3])
