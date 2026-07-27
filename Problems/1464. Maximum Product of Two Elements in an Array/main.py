# LeetCode: 1464 
# Problem: Maximum Product of Two Elements in an Array

# Primary Topic:
# - Array

# Secondary Topics:
# - None

# Time Complexity: O(n)
# Space Complexity: O(1)

# Author: Atulit


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        highest = 0
        sec_highest = 0
        for i in nums:
            if i>highest:
                sec_highest = highest
                highest = i
            elif (i>sec_highest):
                sec_highest = i

        return (highest-1)*(sec_highest-1)