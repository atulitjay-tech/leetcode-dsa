# LeetCode: 1047
# Problem: Remove All Adjacent Duplicates In String

# Primary Topic:
# - Stack

# Secondary Topics:
# - String

# Time Complexity: O(n)
# Space Complexity: O(n)

# Author: Atulit


class Solution:
    def removeDuplicates(self, s: str) -> str:
        l = []

        for i in s:
            if not l or i != l[-1]:
                l.append(i)
            else:
                l.pop()

        return "".join(l)