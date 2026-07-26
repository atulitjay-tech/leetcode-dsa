# LeetCode: 3658
# Problem: GCD of Odd and Even Sums

# Primary Topic:
# - a

# Secondary Topics:
# - Number Theory

# Time Complexity: O(1)
# Space Complexity: O(1)

# Author: Atulit
 

class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        if not nums:
            return []
        
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0
        
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
                
        result = []
        threshold = len(nums) // 3
        
        actual_count1 = nums.count(candidate1) if candidate1 is not None else 0
        actual_count2 = nums.count(candidate2) if candidate2 is not None else 0
        
        if actual_count1 > threshold:
            result.append(candidate1)
        if candidate2 != candidate1 and actual_count2 > threshold:
            result.append(candidate2)
            
        return result