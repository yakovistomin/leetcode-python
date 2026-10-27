import statistics

import pytest
from hypothesis import given, strategies as st

from solutions.p0004_find_median_sorted_arrays import Solution


@pytest.mark.parametrize(
    ('nums1', 'nums2', 'expected'),
    [
        ([1, 3], [2], 2),
        ([1, 2], [3, 4], 2.5),
        ([1, 2], [], 1.5),
        ([1, 2, 3], [], 2),
        ([], [1, 2], 1.5),
        ([], [1, 2, 3], 2),
        ([0], [-1], -0.5),
    ],
)
def test_find_median_sorted_arrays(nums1: list[int], nums2: list[int], expected: float) -> None:
    assert Solution().findMedianSortedArrays(nums1=nums1, nums2=nums2) == pytest.approx(expected)


@given(
    st.lists(
        elements=st.integers(min_value=-(10**6), max_value=10**6),
        min_size=1,
        max_size=2000,
    ),
)
def test_find_median_sorted_arrays_properties(value: list[int]) -> None:
    nums1 = value[: len(value) // 2]
    nums2 = value[len(value) // 2 :]
    nums1.sort()
    nums2.sort()
    value.sort()

    result = Solution().findMedianSortedArrays(nums1=nums1, nums2=nums2)

    assert result == pytest.approx(statistics.median(value))
