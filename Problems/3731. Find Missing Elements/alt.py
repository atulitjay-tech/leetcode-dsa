#2

# LeetCode: 3731
# Problem: Find Missing Elements

# Primary Topic:
# - Array

# Secondary Topics:
# - Binary Search
# - Sorting

# Time Complexity: O(n log n)
# Space Complexity: O(k)

# Author: Atulit


class Solution:
    def findMissingElements(self, nums: list[int]) -> list[int]:
        def found(element, lst):
            a = 0
            b = len(lst) -1
            while a<=b:
                mid = (a+b)//2
                if element == nums[mid]:
                    return True
                elif (nums[mid]>element):
                    b=mid-1
                else:
                    a=mid+1
                    
            return False

        mn = mx = nums[0]
        missing =[]
        nums.sort()
        for i in nums:
            if mx<i:
                mx=i
            if mn>i:
                mn=i

        for i in range(mn,mx):
            if not found(i, nums):
                missing.append(i)

        return missing