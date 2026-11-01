import re

import pytest
from hypothesis import given, strategies as st

from solutions.p0010_regular_expression_matching import Solution


ALPHABET = 'ab'

Token = tuple[str, bool]

tokens = st.lists(
    st.tuples(st.sampled_from(ALPHABET + '.'), st.booleans()),
    min_size=1,
    max_size=8,
)


def to_pattern(parts: list[Token]) -> str:
    return ''.join(char + ('*' if starred else '') for char, starred in parts)


@st.composite
def matching_cases(draw: st.DrawFn) -> tuple[str, str]:
    parts = draw(tokens)
    chars: list[str] = []
    for char, starred in parts:
        count = draw(st.integers(min_value=0, max_value=3)) if starred else 1
        if char == '.':
            chars.append(draw(st.text(alphabet=ALPHABET, min_size=count, max_size=count)))
        else:
            chars.append(char * count)
    return ''.join(chars), to_pattern(parts)


@pytest.mark.parametrize(
    ('value', 'expr', 'expected'),
    [
        ('aa', 'a', False),
        ('aa', 'a*', True),
        ('ab', '.*', True),
        ('aab', 'c*a*b', True),
        ('mississippi', 'mis*is*p*.', False),
        ('ab', '.*c', False),
        ('aaa', 'a*a', True),
        ('a', 'ab*', True),
        ('a', 'a*b*', True),
        ('a', 'aa', False),
    ],
)
def test_is_matched(value: str, expr: str, expected: bool) -> None:
    assert Solution().isMatch(value, expr) is expected


@given(
    s=st.text(alphabet=ALPHABET, min_size=1, max_size=12),
    parts=tokens,
)
def test_matches_reference(s: str, parts: list[Token]) -> None:
    pattern = to_pattern(parts)
    assert Solution().isMatch(s, pattern) is (re.fullmatch(pattern, s) is not None)


@given(matching_cases())
def test_constructed_matches(case: tuple[str, str]) -> None:
    s, pattern = case
    assert Solution().isMatch(s, pattern) is True
