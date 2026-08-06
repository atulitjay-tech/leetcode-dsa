# LeetCode: 3345
# Problem: Smallest Divisible Digit Product I

# Primary Topic:
# - Math

# Secondary Topics:
# - Brute Force
# - Number Theory
# - Digit Manipulation

# Time Complexity: O((result - n) * d), where d is the number of digits in each candidate
# Space Complexity: O(1)

# Author: Atulit


class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        while True:
            temp = str(n)
            p=1
            for i in temp:
                p*=int(i)

            if p%t==0:
                return n
            else:
                n+=1