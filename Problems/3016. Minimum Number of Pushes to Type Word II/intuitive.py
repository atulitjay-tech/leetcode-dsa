# LeetCode: 3016
# Problem: Minimum Number of Pushes to Type Word II

# Primary Topic:
# - String

# Secondary Topics:
# - Greedy
# - Sorting

# Time Complexity: O(n)
# Space Complexity: O(1)

# Author: Atulit


class Solution:
    def minimumPushes(self, word: str) -> int:
        
        freq = [0]*26
        for i in word:
            freq[ord(i) - 97] += 1
        
        freq.sort(reverse = True)

        alph = 0
        cost = 0


        for i in freq:
            if alph<8:
                cost+=i
            elif alph>=8 and alph<16:
                cost+=2*i
            elif alph>=16 and alph<24:
                cost+=3*i
            else:
                cost+=4*i

            alph+=1
        
        return cost