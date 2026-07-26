# LeetCode: 1291
# Problem: Sequential Digits

# Primary Topic:
# - Math

# Secondary Topics:
# - Number Theory

# Time Complexity: O(1)
# Space Complexity: O(1)

# Author: Atulit
 

class Solution:

    def sequentialDigits(self, low: int, high: int) -> list[int]:
        sample = "123456789"
        result = []

        low_len = len(str(low))
        high_len = len(str(high))

        for length in range(low_len, high_len + 1):
            for start in range(10 - length):
                end = start + length
                num = int(sample[start:end])

                if low <= num <= high:
                    result.append(num)

        return result