from typing import Protocol

import pytest
from hypothesis import given, strategies as st

from solutions.p0005_longest_palindrome import DynamicProgrammingSolution, ExpandFromCenterSolution


class LongestPolindromeSolutionProtocol(Protocol):
    def longestPalindrome(self, s: str) -> str: ...


IMPLEMENTATIONS = (DynamicProgrammingSolution, ExpandFromCenterSolution)

by_implementation = pytest.mark.parametrize('implementation', IMPLEMENTATIONS, ids=lambda cls: cls.__name__)


@by_implementation
@pytest.mark.parametrize(
    ('value', 'expected'),
    [
        ('babad', 'bab'),
        ('cbbd', 'bb'),
        ('a', 'a'),
        ('abcd', 'a'),
        ('abca', 'a'),
        ('babadxxxoxox', 'xoxox'),
        ('aaabaa', 'aabaa'),
    ],
)
def test_longest_palindrome(implementation: type[LongestPolindromeSolutionProtocol], value: str, expected: str) -> None:
    assert implementation().longestPalindrome(s=value) == expected


def brute_force(value: str) -> str:
    n = len(value)
    for length in range(n, 0, -1):
        for start in range(n - length + 1):
            sub = value[start : start + length]
            if sub == sub[::-1]:
                return sub
    return ''


@by_implementation
@given(st.text(alphabet='abc', min_size=1, max_size=40))
def test_longest_palindrome_properties(implementation: type[LongestPolindromeSolutionProtocol], value: str) -> None:
    expected = brute_force(value)

    result = implementation().longestPalindrome(s=value)

    assert result == expected
