import re

import pytest

from solutions.p0012_integer_to_roman import ROMAN_INT_MAP, Solution


ROMAN_VALUES = dict(ROMAN_INT_MAP[::-1])
CANONICAL_ROMAN = re.compile(r'M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})')


def roman_to_int(roman: str) -> int:
    total = 0
    for current, following in zip(roman, [*roman[1:], None], strict=True):
        value = ROMAN_VALUES[current]
        if following is not None and value < ROMAN_VALUES[following]:
            total -= value
        else:
            total += value
    return total


@pytest.mark.parametrize(('num', 'expected'), [(3749, 'MMMDCCXLIX'), (58, 'LVIII'), (1994, 'MCMXCIV')])
def test_int_to_roman(num: int, expected: str) -> None:
    assert Solution().intToRoman(num=num) == expected


@pytest.mark.parametrize('num', range(1, 4000))
def test_int_to_roman_exhaustive(num: int) -> None:
    roman = Solution().intToRoman(num=num)

    assert roman
    assert CANONICAL_ROMAN.fullmatch(roman)
    assert roman_to_int(roman) == num
