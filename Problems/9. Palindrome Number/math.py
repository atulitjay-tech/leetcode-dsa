# LeetCode: 9
# Problem: Palindrome Number

# Primary Topic:
# - Math

# Secondary Topics:
# - None

# Time Complexity: O(logx)
# Space Complexity: O(1)

# Author: Atulit


class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        rev = 0
        if abs(x) != x:
            return False

        while temp:
            d = temp%10
            rev = rev*10 + d
            temp//=10
        
        if rev == x:
            return True
        else:
            return False