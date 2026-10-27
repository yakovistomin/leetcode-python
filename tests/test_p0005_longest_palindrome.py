import pytest
from hypothesis import given, strategies as st

from solutions.p0005_longest_palindrome import Solution


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
def test_longest_palindrome(value: str, expected: str) -> None:
    assert Solution().longestPalindrome(s=value) == expected


def brute_force(value: str) -> str:
    n = len(value)
    for length in range(n, 0, -1):
        for start in range(n - length + 1):
            sub = value[start : start + length]
            if sub == sub[::-1]:
                return sub
    return ''


@given(st.text(alphabet='abc', min_size=1, max_size=40))
def test_longest_palindrome_properties(value: str) -> None:
    expected = brute_force(value)

    result = Solution().longestPalindrome(s=value)

    assert result == expected
