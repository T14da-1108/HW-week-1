import pytest
import math
from .assert_task import divide

from typing import Callable



def divide_numbers(a: int,b: int) -> float:
    """Divides a by b"""
    if b == 0:
           raise ZeroDivisionError("division by zero")
    return a / b

def is_function_docstring_exists(func: Callable) -> bool:
    """Check if a function has a docstring.
    """
    return bool(func.__doc__)

def test_division_simple() -> None:
    result = divide_numbers(1, 4) #use divide_numbers instead of divide
    assert isinstance(result, float)
    assert result == 0.25
    assert is_function_docstring_exists(divide_numbers), "Docstring for 'divide' is missing."


def test_division_negative() -> None:
    result = divide(a=-9, b=27)
    assert isinstance(result, float)
    assert math.isclose(result, -0.333333333)


def test_divide_by_zero_assert() -> None:
    with pytest.raises(ZeroDivisionError, match="division by zero"):
        divide(5, 0)
