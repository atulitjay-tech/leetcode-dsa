# LeetCode: 4
# Problem: Median of Two Sorted Arrays

# Primary Topic:
# - Binary Search

# Secondary Topics:
# - Array
# - Divide and Conquer

# Time Complexity: O(log(min(m, n)))
# Space Complexity: O(1)

# Author: Atulit


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total_len = m + n
        half = (total_len + 1) // 2

        left, right = 0, m

        while left <= right:
            i = (left + right) // 2
            j = half - i

            left_max_1 = nums1[i - 1] if i > 0 else float('-inf')
            right_min_1 = nums1[i] if i < m else float('inf')
            left_max_2 = nums2[j - 1] if j > 0 else float('-inf')
            right_min_2 = nums2[j] if j < n else float('inf')

            if left_max_1 <= right_min_2 and left_max_2 <= right_min_1:
                if total_len % 2 == 0:
                    return (max(left_max_1, left_max_2) + min(right_min_1, right_min_2)) / 2.0
                return float(max(left_max_1, left_max_2))

            if left_max_1 > right_min_2:
                right = i - 1
            else:
                left = i + 1