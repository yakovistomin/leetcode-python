from math import inf


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        len1, len2 = len(nums1), len(nums2)
        total = len1 + len2
        half = total // 2

        lo, hi = 0, len1

        while lo <= hi:
            idx1 = (lo + hi) // 2
            idx2 = half - idx1

            val1_l = nums1[idx1 - 1] if idx1 > 0 else -inf
            val1_r = nums1[idx1] if idx1 < len1 else inf
            val2_l = nums2[idx2 - 1] if idx2 > 0 else -inf
            val2_r = nums2[idx2] if idx2 < len2 else inf

            if val1_l > val2_r:
                hi = idx1 - 1
            elif val2_l > val1_r:
                lo = idx1 + 1
            else:
                min_r = min(val1_r, val2_r)
                if total % 2:
                    return min_r
                return (max(val1_l, val2_l) + min_r) / 2

        raise AssertionError('Unreacheble')

    def findMedianSortedArraysUnoptimized(self, nums1: list[int], nums2: list[int]) -> float:
        nums_len = len(nums1) + len(nums2)
        if nums_len == 0:
            raise ValueError('Both arrays are empty')

        idx1 = idx2 = 0
        prev_num = cur_num = 0

        for _ in range(nums_len // 2 + 1):
            prev_num = cur_num

            if idx1 >= len(nums1) or (idx2 < len(nums2) and nums2[idx2] < nums1[idx1]):
                cur_num = nums2[idx2]
                idx2 += 1
            else:
                cur_num = nums1[idx1]
                idx1 += 1

        return cur_num if nums_len % 2 else (cur_num + prev_num) / 2
