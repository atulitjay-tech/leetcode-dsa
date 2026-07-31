# LeetCode: 3016
# Problem: Minimum Number of Pushes to Type Word II

# Primary Topic:
# - String

# Secondary Topics:
# - Greedy
# - Sorting

# Time Complexity: O(n)
# Space Complexity: O(1)

# Author: Atulit


from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = Counter(word).values()
        
        arr = sorted(counts, reverse=True)
        
        cost = 0
        for i, c in enumerate(arr):
            cost += c * (i // 8 + 1)
            
        return cost