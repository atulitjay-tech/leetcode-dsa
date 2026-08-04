#1

# LeetCode: 3731
# Problem: Find Missing Elements

# Primary Topic:
# - Array

# Secondary Topics:
# - Hashing

# Time Complexity: O(n)
# Space Complexity: O(n)

# Author: Atulit



class Solution:
    def findMissingElements(self, nums: list[int]) -> list[int]:
        
        dic = {nums[i]: True for i in range(len(nums))}

        missing =[]
        for i in range(min(nums),max(nums)):
            if i not in dic:
                missing.append(i)

        return missing