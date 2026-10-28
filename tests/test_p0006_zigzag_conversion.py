import string
from collections import Counter

import pytest
from hypothesis import given, strategies as st

from solutions.p0006_zigzag_conversion import Solution


@pytest.mark.parametrize(
    ('value', 'num_rows', 'expected'),
    [
        ('PAYPALISHIRING', 3, 'PAHNAPLSIIGYIR'),
        ('PAYPALISHIRING', 4, 'PINALSIGYAHRPI'),
        ('A', 1, 'A'),
        ('AB', 1, 'AB'),
        ('AB', 3, 'AB'),
        ('ABCD', 2, 'ACBD'),
    ],
)
def test_convert(value: str, num_rows: int, expected: str) -> None:
    assert Solution().convert(s=value, num_rows=num_rows) == expected


def reference_convert(s: str, num_rows: int) -> str:
    if num_rows == 1:
        return s

    rows: list[list[str]] = [[] for _ in range(num_rows)]
    row, step = 0, 1
    for ch in s:
        rows[row].append(ch)
        if row == 0:
            step = 1
        elif row == num_rows - 1:
            step = -1
        row += step

    return ''.join(''.join(r) for r in rows)


@given(
    s=st.lists(st.sampled_from(string.printable), min_size=1, unique=True).map(''.join),
    num_rows=st.integers(min_value=1, max_value=len(string.printable) + 10),
)
def test_convert_matches_reference(s: str, num_rows: int) -> None:
    assert Solution().convert(s, num_rows) == reference_convert(s, num_rows)


@given(
    s=st.text(alphabet=string.printable, min_size=1, max_size=500),
    num_rows=st.integers(min_value=1, max_value=1000),
)
def test_convert_is_permutation(s: str, num_rows: int) -> None:
    result = Solution().convert(s, num_rows)

    assert Counter(result) == Counter(s)
    if num_rows == 1 or num_rows >= len(s):
        assert result == s
