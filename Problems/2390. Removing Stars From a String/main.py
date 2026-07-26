# LeetCode: 3658
# Problem: GCD of Odd and Even Sums

# Primary Topic:
# - Math

# Secondary Topics:
# - Number Theory

# Time Complexity: O(1)
# Space Complexity: O(1)

# Author: Atulit


class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch == "*":
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)