import pytest

from leetcode_problems.problem_1_two_sum import Solution


@pytest.mark.parametrize(
    ('nums', 'target', 'expected_result'),
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ],
)
def test_two_sum(nums: list[int], target: int, expected_result: list[int]) -> None:
    assert Solution().twoSum(nums=nums, target=target) == expected_result
