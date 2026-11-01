import pytest
from hypothesis import given, strategies as st

from solutions.p0011_container_with_most_water import Solution


def brute_force_max_area(height: list[int]) -> int:
    best = 0
    for i in range(len(height)):
        for j in range(i + 1, len(height)):
            best = max(best, min(height[i], height[j]) * (j - i))
    return best


@pytest.mark.parametrize(
    ('height', 'expected'),
    [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([0, 0], 0),
        ([1, 2, 3, 4, 5], 6),
        ([5, 4, 3, 2, 1], 6),
        ([3, 1, 1, 1, 3], 12),
        ([1, 3, 2, 5, 25, 24, 5], 24),
    ],
)
def test_max_area(height: list[int], expected: int) -> None:
    assert Solution().maxArea(height=height) == expected


@given(st.lists(st.integers(min_value=0, max_value=10), min_size=2, max_size=50))
def test_max_area_matches_brute_force(height: list[int]) -> None:
    assert Solution().maxArea(height=height) == brute_force_max_area(height)


@given(st.lists(st.integers(min_value=0, max_value=10_000), min_size=2, max_size=50))
def test_max_area_full_range(height: list[int]) -> None:
    assert Solution().maxArea(height=height) == brute_force_max_area(height)
