# LeetCode: 3517
# Problem: Smallest Palindromic Rearrangement I

# Primary Topic:
# - String

# Secondary Topics:
# - Hashing

# Time Complexity: O(n + 26)
# Space Complexity: O(1)

# Author: Atulit


class Solution:
    def smallestPalindrome(self, s: str) -> str:
        ch_count = [0] * 26
        for char in s:
            ch_count[ord(char) - ord('a')] += 1
            
        lhalf = []
        mid_char = ""
        if (len(s) % 2 ==1):
            mid_char = s[len(s)//2]
        
        for i in range(26):
            if ch_count[i] == 0:
                continue
                
            char = chr(i + ord('a'))
                            
            lhalf.append(char * (ch_count[i] // 2))
            
        lstr = "".join(lhalf)
        
        return lstr + mid_char + lstr[::-1]