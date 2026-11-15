import pytest

from solutions.p0013_roman_to_integer import Solution


@pytest.mark.parametrize(('value', 'expected'), [('III', 3), ('LVIII', 58), ('MCMXCIV', 1994), ('XL', 40)])
def test_roman_to_int(value: str, expected: int) -> None:
    assert Solution().romanToInt(s=value) == expected
