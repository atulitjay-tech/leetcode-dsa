# LeetCode: 2390
# Problem: Removing Stars From a String

# Primary Topic:
# - Stack

# Secondary Topics:
# - String

# Time Complexity: O(n)
# Space Complexity: O(n)

# Author: Atulit


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        cond1 = word == word.upper()
        cond2 = word == word.lower()
        cond3 = word == word.capitalize()
        return (cond1 or cond2 or cond3)