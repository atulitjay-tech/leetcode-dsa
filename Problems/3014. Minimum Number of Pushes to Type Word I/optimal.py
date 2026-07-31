# LeetCode: 3014
# Problem: Minimum Number of Pushes to Type Word I

# Primary Topic:
# - String

# Secondary Topics:
# - Greedy
# - Math

# Time Complexity: O(1)
# Space Complexity: O(1)

# Author: Atulit


class Solution:
    def minimumPushes(self, word: str) -> int:
        ans = 0
        for i in range(len(word)):
            ans += i // 8 + 1
        return ans