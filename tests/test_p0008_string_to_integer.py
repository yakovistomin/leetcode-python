import re

import pytest
from hypothesis import given, strategies as st

from solutions.p0008_string_to_integer import Solution


INT_MIN = -(2**31)
INT_MAX = 2**31 - 1
ATOI_RE = re.compile(r' *([+-]?\d+)', re.ASCII)


def reference_atoi(s: str) -> int:
    match = ATOI_RE.match(s)
    if match is None:
        return 0
    return max(INT_MIN, min(INT_MAX, int(match.group(1))))


@st.composite
def number_like(draw: st.DrawFn) -> str:
    spaces = draw(st.text(alphabet=' ', max_size=3))
    sign = draw(st.sampled_from(['', '+', '-']))
    zeros = draw(st.text(alphabet='0', max_size=3))
    number = draw(
        st.one_of(
            st.integers(min_value=0, max_value=10**12),
            st.integers(min_value=2**31 - 3, max_value=2**31 + 3),
        ),
    )
    tail = draw(st.text(alphabet=' +-0123a.', max_size=5))
    return f'{spaces}{sign}{zeros}{number}{tail}'


@given(number_like())
def test_my_atoi_numbers(s: str) -> None:
    assert Solution().myAtoi(s) == reference_atoi(s)


@given(st.text(alphabet=' \t+-0123a', max_size=12))
def test_my_atoi_noise(s: str) -> None:
    assert Solution().myAtoi(s) == reference_atoi(s)


@pytest.mark.parametrize(
    ('value', 'expected'),
    [
        ('', 0),
        ('    ', 0),
        ('-', 0),
        ('42', 42),
        (' -042', -42),
        ('1337c0d3', 1337),
        ('0-1', 0),
        ('words and 987', 0),
        ('2147483648', 2**31 - 1),
        ('-2147483649', -(2**31)),
        ('9' * 200, 2**31 - 1),
        ('-' + '9' * 200, -(2**31)),
    ],
)
def test_my_atoi(value: str, expected: int) -> None:
    assert Solution().myAtoi(value) == expected
