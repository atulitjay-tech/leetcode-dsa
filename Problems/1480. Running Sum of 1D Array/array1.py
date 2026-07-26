# LeetCode: 1480
# Problem: Running Sum of 1D Array

# Primary Topic:
# - Arrays

# Secondary Topics:
# - None

# Time Complexity: O(n)
# Space Complexity: O(n)

# Author: Atulit
 

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningsum=[]
        for i in range (len(nums)):
            if i==0:
                runningsum.append(nums[0])
            else:
                runningsum.append(runningsum[i-1] + nums[i])
        
        return runningsum