# LeetCode: 26
# Problem: Remove Duplicates from Sorted Array

# Primary Topic:
# - Arrays

# Secondary Topics:
# - Two Pointers

# Time Complexity: O(n)
# Space Complexity: O(1)

# Author: Atulit
 

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        z=0
        last_unq = nums[0]
        for i in range (len(nums)):
            if nums[i] != nums[z]:
                last_unq = nums[i]
                z+=1
                nums[z] = nums[i]

        return z+1