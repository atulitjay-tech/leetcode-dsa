# LeetCode: 1855
# Problem: Maximum Distance Between a Pair of Values

# Primary Topic:
# - Arrays

# Secondary Topics:
# - Two Pointers

# Time Complexity: O(m + n)
# Space Complexity: O(1)

# Author: Atulit


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        i = 0
        
        for j in range(n):
            if nums1[i] > nums2[j]:
                i += 1
                if i >= m:
                    break

        return max(j - i, 0)