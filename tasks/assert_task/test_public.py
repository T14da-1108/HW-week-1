import pytest
import testlib
import math

from .assert_task import divide


###################
# Structure asserts
###################

def test_docs() -> None:
    assert testlib.is_function_docstring_exists(divide)


###################
# Tests
###################


def test_division_simple() -> None:
    result = divide(1, 4)
    assert isinstance(result, float)
    assert result == 0.25


def test_division_negative() -> None:
    result = divide(-9, 27)
    assert isinstance(result, float)
    assert math.isclose(result, -0.333333333)


def test_divide_by_zero_assert() -> None:
    with pytest.raises(AssertionError, match="Division by zero"):
        divide(5, 0)
