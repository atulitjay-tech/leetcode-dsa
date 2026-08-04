#1

# LeetCode: 3731
# Problem: Find Missing Elements

# Primary Topic:
# - Array

# Secondary Topics:
# - Searching

# Time Complexity: O(n^2)
# Space Complexity: O(k)           ....    k is the number of missing elements

# Author: Atulit


class Solution:
    def findMissingElements(self, nums: list[int]) -> list[int]:
        mn = mx = nums[0]
        missing =[]

        for i in nums:
            if mx<i:
                mx=i
            if mn>i:
                mn=i

        for i in range(mn,mx):
            if i not in nums:
                missing.append(i)

        return missing