class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
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
