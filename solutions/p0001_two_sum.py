class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        index: dict[int, int] = {}

        for idx, value in enumerate(nums):
            first_value = target - value
            if first_value in index:
                return [index[first_value], idx]
            index[value] = idx

        raise ValueError('Not found')
