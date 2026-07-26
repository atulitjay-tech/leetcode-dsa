# LeetCode: 7
# Problem: Reverse String

# Primary Topic:
# - String Manipulation

# Secondary Topics:
# - None

# Time Complexity: O(n)
# Space Complexity: O(1)

# Author: Atulit


class Solution:
    def reverse(self, x: int) -> int:
        temp = str (x)
        rev=""
        for i in temp:
            rev = i + rev 
        
        if(rev[-1] == "-"):
            rev = int("-"+rev[0:-1:1])
        else:
            rev = int(rev)
            
        if -2**31 <= rev and rev<= 2**31 - 1:
            return rev
        else:
            return (0)