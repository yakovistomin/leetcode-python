import pytest

from solutions.p0014_longest_common_prefix import Solution


@pytest.mark.parametrize(
    ('strs', 'expected'),
    [(['flower', 'flow', 'flight'], 'fl'), (['dog', 'racecar', 'car'], '')],
)
def test_longest_common_prefix(strs: list[str], expected: str) -> None:
    assert Solution().longestCommonPrefix(strs=strs) == expected
