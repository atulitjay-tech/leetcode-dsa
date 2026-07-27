# LeetCode: 229
# Problem: Majority Element II

# Primary Topic:
# - Array

# Secondary Topics:
# - Boyer-Moore Voting
# - Hashing

# Time Complexity: O(n)
# Space Complexity: O(1)

# Author: Atulit
 

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 0:
            return False
        return (n&(n-1)==0) and n%3==1