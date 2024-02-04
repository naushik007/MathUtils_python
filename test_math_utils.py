from math_utils import MathUtils
import pytest

@pytest.mark.parametrize("a, b, expected_result", [
    (5, 3, 8),
    (10, 4, 6),
    (-2, 1, -3),
])
def test_add(a, b, expected_result):
    math_utils = MathUtils()
    result = math_utils.add(a, b)
    assert result == expected_result

@pytest.mark.parametrize("a, b, expected_result", [
    (10, 4, 6),
    (15, 3, 12),
    (-5, 2, -7),
])
def test_subtract(a, b, expected_result):
    math_utils = MathUtils()
    result = math_utils.subtract(a, b)
    assert result == expected_result

# Similar test cases for multiply and divide methods
@pytest.mark.parametrize("a, b, expected_result", [
    (15, 3, 5.0),
    (8, 2, 4.0),
    (-10, 2, -5.0),
])
def test_divide_valid(a, b, expected_result):
    math_utils = MathUtils()
    result = math_utils.divide(a, b)
    assert result == expected_result

@pytest.mark.parametrize("a, b", [
    (10, 0),
    (-5, 0),
])
def test_divide_by_zero(a, b):
    math_utils = MathUtils()
    with pytest.raises(ZeroDivisionError):
        math_utils.divide(a, b)