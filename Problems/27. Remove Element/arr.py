# LeetCode: 27
# Problem: Remove Element

# Primary Topic:
# - Arrays

# Secondary Topics:
# - Two Pointers

# Time Complexity: O(n)
# Space Complexity: O(1)

# Author: Atulit
 

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0 
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k