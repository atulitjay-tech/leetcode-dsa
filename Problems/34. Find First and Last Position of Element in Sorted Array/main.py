# LeetCode: 520
# Problem: Detect Capital

# Primary Topic:
# - String

# Secondary Topics:
# - None

# Time Complexity: O(n)
# Space Complexity: O(1)

# Author: Atulit


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        i = 0
        j = len(nums) - 1

        while (i<=j):
            m=(i+j)//2
            if (nums[m] != target):
                if nums[m]<target:
                    i=m+1 
                else:
                    j=m-1
            else:
                a=b=m

                while True:
                    c=0
                    d=0
                    if a == 0 and b == len(nums) - 1:
                        break

                    if a!= 0 and nums[a] == nums[a-1]:
                        a-=1
                    else:
                        c+=1
                    if b!=len(nums)-1 and nums[b] == nums[b+1]:
                        b+=1
                    else:
                        c+=1

                    if c==2:
                        break
                
                return [a,b]

        return [-1,-1]