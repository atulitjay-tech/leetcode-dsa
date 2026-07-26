# LeetCode: 3658
# Problem: GCD of Odd and Even Sums

# Primary Topic:
# - a

# Secondary Topics:
# - Number Theory

# Time Complexity: O(1)
# Space Complexity: O(1)

# Author: Atulit
 


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n <= 0:
            return False
        return (n&(n-1)==0)