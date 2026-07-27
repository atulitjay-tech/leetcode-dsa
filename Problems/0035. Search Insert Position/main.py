# LeetCode: 3658
# Problem: GCD of Odd and Even Sums

# Primary Topic:
# - Math

# Secondary Topics:
# - Number Theory

# Time Complexity: O(1)
# Space Complexity: O(1)

# Author: Atulit
 

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        i=0
        j=len(nums)-1

        while i<=j:

            m= (i+j)//2

            if nums[m] == target:
                return m

            elif nums[m] > target:
                j=m-1
                if m==0:
                    return 0
                if nums[m-1] < target:
                    return m

            else:
                i=m+1
                if m==len(nums)-1:
                    return m+1
                if nums[m+1] > target:
                    return m+1
