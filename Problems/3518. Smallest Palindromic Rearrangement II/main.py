#this question was really difficult for me and i was unable to come up with a solution even after trying for 2 hours.. so the solution is not completely authentically made by me :)

# LeetCode: 3518
# Problem: Smallest Palindromic Rearrangement II

# Primary Topic:
# - String

# Secondary Topics:
# - Hashing
# - Combinatorics

# Time Complexity: O(n + 26^2)
# Space Complexity: O(1)

# Author: Atulit


from collections import comb 
class Solution:
    def smallestPalindrome (self, s: str, k: int) -> str:
        n = len(s)
        half = n // 2
        freq = [0] * 26
        for i in range(half): freq[ord(s[i]) - ord('a')] += 1

        def perm(rem):
            acc =1
            for ci in range(26):
                f = freq[ci]
                if not f: continue
                if f > rem: return 0
                acc *= comb(rem, f)
                if acc > k: return acc
                rem -= f
            return acc
        
        left = []
        start = 0
        for i in range(half):
            selected = False
            for ci in range(26):
                if not freq[ci]: continue
                freq[ci] -= 1

                p = perm(half -i -1)
                if start + p >= k:
                    left.append(chr(ci + ord('a')))
                    selected = True
                    break
                    
                freq[ci] += 1
                start += p

            if not selected: return ""

        h1 = "".join(left)
        mid = s[n//2] if n % 2 == 1 else ""
        h2 = "".join(left[::-1])
        return h1 + mid + h2