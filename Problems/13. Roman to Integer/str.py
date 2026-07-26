# LeetCode: 13
# Problem: Roman to Integer

# Primary Topic:
# - Strings

# Secondary Topics:
# - Math
# - Hashing

# Time Complexity: O(n)
# Space Complexity: O(1)

# Author: Atulit
 

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }

        total = 0

        for i in range(len(s)):
            if i+1 <len(s) and roman[s[i]] < roman[s[1+i]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]
        return total