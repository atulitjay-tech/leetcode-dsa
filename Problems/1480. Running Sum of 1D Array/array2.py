# LeetCode: 1480
# Problem: Running Sum of 1D Array

# Primary Topic:
# - Arrays

# Secondary Topics:
# - None

# Time Complexity: O(n)
# Space Complexity: O(1)

# Author: Atulit


class Solution:
    def runningSum(self, nums):
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]

        return nums