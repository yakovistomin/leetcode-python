import pytest
from hypothesis import given, settings, strategies as st

from solutions.p0003_longest_substring_without_repeating_characters import Solution


@pytest.mark.parametrize(
    ('value', 'expected'),
    [
        ('abcabcbb', 3),
        ('bbbbb', 1),
        ('pwwkew', 3),
        ('', 0),
        ('a', 1),
    ],
)
def test_length_of_longest_substring(value: str, expected: int) -> None:
    assert Solution().lengthOfLongestSubstring(value) == expected


def brute_force(s: str) -> int:
    result = 0

    for i in range(len(s)):
        seen = set()

        for j in range(i, len(s)):
            if s[j] in seen:
                break

            seen.add(s[j])
            result = max(result, len(seen))

    return result


@settings(max_examples=500)
@given(
    st.text(
        alphabet=st.characters(min_codepoint=97, max_codepoint=122),
        min_size=0,
        max_size=100,
    ),
)
def test_length_of_longest_substring_properties(value: str) -> None:
    expected = brute_force(value)

    result = Solution().lengthOfLongestSubstring(value)

    assert result == expected
