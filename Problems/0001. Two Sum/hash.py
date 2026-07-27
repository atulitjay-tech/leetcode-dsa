# LeetCode: 1
# Problem: Two Sum

# Primary Topic:
# - Hash Table

# Secondary Topics:
# - Two Pointers  (not used in this solution)

# Time Complexity: O(n)
# Space Complexity: O(n)

# Author: Atulit
 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for index, num in enumerate(nums):
            complement = target - num
            
            if complement in seen:
                return [seen[complement], index]
            
            seen[num] = index