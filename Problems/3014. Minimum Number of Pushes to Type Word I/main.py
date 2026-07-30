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
    def minimumPushes(self, word: str) -> int:
        l = len(word)
        cost=l

        if l>8:
            cost+=l-8
        if l>16:
            cost+=l-16
        if l>24:
            cost+=l-24
            
        return cost