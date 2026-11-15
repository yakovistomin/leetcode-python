import pytest

from solutions.p0012_integer_to_roman import Solution


@pytest.mark.parametrize(('num', 'expected'), [(3749, 'MMMDCCXLIX'), (58, 'LVIII'), (1994, 'MCMXCIV'), (40, 'XL')])
def test_int_to_roman(num: int, expected: str) -> None:
    assert Solution().intToRoman(num=num) == expected
