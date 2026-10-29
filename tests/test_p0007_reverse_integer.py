import pytest
from hypothesis import given, strategies as st

from solutions.p0007_reverse_integer import Solution


INT_MIN = -(2**31)
INT_MAX = 2**31 - 1


@pytest.mark.parametrize(
    ('value', 'expected'),
    [
        (123, 321),
        (-123, -321),
        (120, 21),
        (-120, -21),
        (-10, -1),
        (0, 0),
        (1_534_236_469, 0),
        (1_463_847_412, 2_147_483_641),
        (-1_463_847_412, -2_147_483_641),
        (-1_534_236_469, 0),
    ],
)
def test_reverse(value: int, expected: int) -> None:
    assert Solution().reverse(value) == expected


def reference_reverse(x: int) -> int:
    sign = -1 if x < 0 else 1
    result = sign * int(str(abs(x))[::-1])
    return result if INT_MIN <= result <= INT_MAX else 0


@given(st.integers(min_value=INT_MIN, max_value=INT_MAX))
def test_reverse_matches_reference(x: int) -> None:
    assert Solution().reverse(x) == reference_reverse(x)
