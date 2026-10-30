import string
from typing import Protocol

import pytest
from hypothesis import assume, given, strategies as st

from solutions.p0009_palindrome_number import CompareEndsSolution, ReverseHalfSolution


INT_MIN = -(2**31)
INT_MAX = 2**31 - 1
IMPLEMENTATIONS = (ReverseHalfSolution, CompareEndsSolution)

by_implementation = pytest.mark.parametrize('implementation', IMPLEMENTATIONS, ids=lambda cls: cls.__name__)


class SolutionProtocol(Protocol):
    def isPalindrome(self, x: int) -> bool: ...


def reference_is_palindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]


@st.composite
def palindromes(draw: st.DrawFn) -> int:
    half = str(draw(st.integers(min_value=1, max_value=99_999)))
    middle = draw(st.sampled_from(['', *string.digits]))
    value = int(half + middle + half[::-1])
    assume(value <= INT_MAX)
    return value


@by_implementation
@pytest.mark.parametrize(
    ('value', 'expected'),
    [
        (121, True),
        (-121, False),
        (10, False),
        (0, True),
        (7, True),
        (1221, True),
        (9079, False),
        (501105, True),
        (123761261, False),
        (1_234_554_321, True),
        (2_147_447_412, True),
        (INT_MAX, False),
        (INT_MIN, False),
    ],
)
def test_is_palindrome(implementation: type[SolutionProtocol], value: int, expected: bool) -> None:
    assert implementation().isPalindrome(value) is expected


@by_implementation
@given(st.integers(min_value=INT_MIN, max_value=INT_MAX))
def test_matches_reference(implementation: type[SolutionProtocol], value: int) -> None:
    assert implementation().isPalindrome(value) is reference_is_palindrome(value)


@by_implementation
@given(palindromes())
def test_constructed_palindromes(implementation: type[SolutionProtocol], value: int) -> None:
    assert implementation().isPalindrome(value) is True


@by_implementation
@given(st.integers(min_value=1, max_value=INT_MAX // 10))
def test_trailing_zero_is_not_palindrome(implementation: type[SolutionProtocol], value: int) -> None:
    assert implementation().isPalindrome(value * 10) is False
