# LeetCode: 28
# Problem: Find the Index of the First Occurrence in a String

# Primary Topic:
# - Strings

# Secondary Topics:
# - 

# Time Complexity: O(n^2)
# Space Complexity: O(n)

# Author: Atulit
 

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        lst= []
        for i in needle:
            lst.append(i)

        for i, ch in enumerate(haystack):
            if ch == lst[0]:
                for j,cha in enumerate(lst):
                    try:
                        if cha != haystack[i+j]:
                            break
                    except:
                        break
                else:
                    return i
        return -1