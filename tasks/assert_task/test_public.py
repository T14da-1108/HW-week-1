import pytest
import math
from .assert_task import divide


def is_function_docstring_exists(func):
    """
    check if a function has a docstring.
    param func: Function to check
    return: True if the function has a docstring, False otherwise
    """
    return bool(func.__doc__)

def divide(a,b):
    """Divides a by b"""
    return a/b

def  is_function_docstring_exists(func):
    return func.__doc__ is not None
assert is_function_docstring_exists(divide), "Docstring for 'divide' is missing."
def test_division_simple() -> None:
    result = divide(1, 4)
    assert isinstance(result, float)
    assert result == 0.25


def test_division_negative() -> None:
    result = divide(a=-9, b=27)
    assert isinstance(result, float)
    assert math.isclose(result, -0.333333333)


def test_divide_by_zero_assert() -> None:
    with pytest.raises(ZeroDivisionError, match="division by zero"):
        divide(5, 0)
