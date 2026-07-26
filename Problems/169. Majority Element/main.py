# LeetCode: 2390
# Problem: Removing Stars From a String

# Primary Topic:
# - Stack

# Secondary Topics:
# - String

# Time Complexity: O(n)
# Space Complexity: O(n)

# Author: Atulit


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        maj=nums[0]
        f=0
        for i in nums:
            if i == maj:
                f+=1
            else:
                f-=1

            if f==0:
                f=1
                maj=i
        
        return maj