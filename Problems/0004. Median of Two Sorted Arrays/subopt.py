# LeetCode: 4
# Problem: Median of Two Sorted Arrays

# Primary Topic:
# - Two Pointers

# Secondary Topics:
# - Array

# Time Complexity: O(m+n)
# Space Complexity: O(1)

# Author: Atulit


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        #sub optimal approach

        m, n = len(nums1), len(nums2)
        total_len = m + n
        
        p1, p2 = 0, 0
        
        curr, prev = 0, 0
        
        for _ in range((total_len // 2) + 1):
            prev = curr
            
            if p1 < m and (p2 >= n or nums1[p1] <= nums2[p2]):
                curr = nums1[p1]
                p1 += 1
            else:
                curr = nums2[p2]
                p2 += 1
                
        if total_len % 2 != 0:
            return float(curr)
        
        return (prev + curr) / 2.0