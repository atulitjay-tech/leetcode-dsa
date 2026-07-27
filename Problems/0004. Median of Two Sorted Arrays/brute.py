# LeetCode: 4
# Problem: Median of Two Sorted Arrays

# Primary Topic:
# - Array

# Secondary Topics:
# - Sorting

# Time Complexity: O((m+n)log(m+n))
# Space Complexity: O(m+n)

# Author: Atulit


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        #brute force
        m=len(nums1)
        n=len(nums2)

        c=nums1+nums2
        c.sort()
        d=m+n - 2

        if (d % 2 == 0):
            return (c[d//2] + c[d//2 + 1])/2
        else:
            return c[(d)//2 + 1]