# LeetCode: 8
# Problem: String to Integer (atoi)

# Primary Topic:
# - String Manipulation

# Secondary Topics:
# - None

# Time Complexity: O(n)
# Space Complexity: O(n)

# Author: Atulit
 

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        num=0
        if s=="":
            return 0

        if(s[0] == "-"):
            z=-1
            s=s[1::]
        elif(s[0] == "+"):
            z=1
            s=s[1::]
        else:
            z=1

        for i in s:
            if i.isdigit():
                num = num*10 + int(i)
            else:
                break

        num*=z
        if num < -2147483648:
            return -2147483648
        if num > 2147483647:
            return 2147483647
        else:   
            return num
        