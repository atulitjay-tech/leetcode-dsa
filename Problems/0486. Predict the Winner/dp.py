# LeetCode: 0486
# Problem: Predict the Winner

# Primary Topic:
# - Dynamic Programming

# Secondary Topics:
# - Recursion
# - Memoization

# Time Complexity: O(n^2)
# Space Complexity: O(n^2)

# Author: Atulit


class Solution:
    def predictTheWinner (self, nums: list[int]) -> bool:
        memo = {}
        def maxDiff(left, right):
            if left == right:
                return nums [left]
            if (left, right) in memo:
                return memo [(left, right)]

            pickLeft = nums [left] - maxDiff (left + 1, right)
            pickRight = nums [right] - maxDiff (left, right - 1)

            memo [(left, right)] = max(pickLeft, pickRight)
            return memo [(left, right)]

        return maxDiff(0, len (nums) - 1) >= 0