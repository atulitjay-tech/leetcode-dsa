# LeetCode: 1358
# Problem: Number of Substrings Containing All Three Characters

# Primary Topic:
# - Hashing

# Secondary Topics:
# - Two Pointers/sliding window

# Time Complexity: O(n)
# Space Complexity: O(1)

# Author: Atulit


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last_seen = {'a': -1, 'b': -1, 'c': -1}
        count = 0
        
        for r, char in enumerate(s):
            last_seen[char] = r
            
            if min(last_seen.values()) != -1:
                count += min(last_seen.values()) + 1
                
        return count