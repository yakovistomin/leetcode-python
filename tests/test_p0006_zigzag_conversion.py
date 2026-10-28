import string
from collections import Counter
from typing import Protocol

import pytest
from hypothesis import given, strategies as st

from solutions.p0006_zigzag_conversion import IndexSolution, SimulationSolution


class ZigzagSolutionProtocol(Protocol):
    def convert(self, s: str, num_rows: int) -> str: ...


IMPLEMENTATIONS = (SimulationSolution, IndexSolution)


by_implementation = pytest.mark.parametrize('implementation', IMPLEMENTATIONS, ids=lambda cls: cls.__name__)


@by_implementation
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
def test_convert(implementation: type[ZigzagSolutionProtocol], value: str, num_rows: int, expected: str) -> None:
    assert implementation().convert(s=value, num_rows=num_rows) == expected


@given(
    s=st.lists(st.sampled_from(string.printable), min_size=1, unique=True).map(''.join),
    num_rows=st.integers(min_value=1, max_value=len(string.printable) + 10),
)
def test_implementations_agree(s: str, num_rows: int) -> None:
    assert SimulationSolution().convert(s, num_rows) == IndexSolution().convert(s, num_rows)


@by_implementation
@given(
    s=st.text(alphabet=string.printable, min_size=1, max_size=500),
    num_rows=st.integers(min_value=1, max_value=1000),
)
def test_convert_is_permutation(implementation: type[ZigzagSolutionProtocol], s: str, num_rows: int) -> None:
    result = implementation().convert(s, num_rows)

    assert Counter(result) == Counter(s)
    if num_rows == 1 or num_rows >= len(s):
        assert result == s
