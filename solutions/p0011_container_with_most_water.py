class Solution:
    def maxArea(self, height: list[int]) -> int:
        l_idx = 0
        r_idx = len(height) - 1
        result = 0

        while l_idx < r_idx:
            l_height = height[l_idx]
            r_height = height[r_idx]
            result = max(result, min(l_height, r_height) * (r_idx - l_idx))

            if l_height < r_height:
                while l_idx < r_idx and height[l_idx] <= l_height:
                    l_idx += 1
            else:
                while l_idx < r_idx and height[r_idx] <= r_height:
                    r_idx -= 1

        return result
