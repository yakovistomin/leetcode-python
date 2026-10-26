import pytest
from hypothesis import given, strategies as st

from solutions.p0001_two_sum import Solution


@pytest.mark.parametrize(
    ('nums', 'target', 'expected'),
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ],
)
def test_two_sum(nums: list[int], target: int, expected: list[int]) -> None:
    assert Solution().twoSum(nums=nums, target=target) == expected


@st.composite
def two_sum_cases(draw: st.DrawFn) -> tuple[list[int], int]:
    nums = draw(
        st.lists(
            st.integers(min_value=-10_000, max_value=10_000),
            min_size=2,
            max_size=100,
        ),
    )

    i = draw(st.integers(min_value=0, max_value=len(nums) - 1))
    j = draw(
        st.integers(min_value=0, max_value=len(nums) - 2),
    )

    if j >= i:
        j += 1

    return nums, nums[i] + nums[j]


@given(two_sum_cases())
def test_two_sum_properties(case: tuple[list[int], int]) -> None:
    nums, target = case

    result = Solution().twoSum(nums, target)

    assert len(result) == 2

    i, j = result

    assert i != j
    assert 0 <= i < len(nums)
    assert 0 <= j < len(nums)
    assert nums[i] + nums[j] == target
