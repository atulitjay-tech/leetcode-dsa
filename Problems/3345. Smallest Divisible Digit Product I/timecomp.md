# Smallest Divisible Digit Product I (LeetCode 3345)

## Problem Overview

Find the smallest integer greater than or equal to `n` such that the product of its digits is divisible by `t`.

## Approach

- Start from `n` and check each integer in ascending order.
- Convert the current number to a string and compute the product of its digits.
- If the digit product is divisible by `t`, return the current number.
- Otherwise, increment the number and repeat.

## Key idea

- The algorithm is a brute-force search with a digit-product check. It is fast enough and uses less memory though.
- Because digit products are limited by number length and digits themselves, the search typically resolves quickly for the values of `t` expected in this problem.

## Time complexity

- Worst-case complexity is `O((result - n) * d)`, where `d` is the number of digits in the current candidate.
- In practice, the loop is bounded by a small constant number of increments for each possible `t` value.

## Effective bounds by `t`

- `t = 1`  -> return `n` immediately.
- `t = 2`  -> at most two iterations; any odd number becomes even after one increment.
- `t = 3`  -> at most three iterations; one of the next few numbers will introduce a digit 3, 6, 9, or 0.
- `t = 4`  -> at most four iterations; one of the next few numbers will include a digit with factor `2 * 2`.
- `t = 5`  -> at most five iterations; one of the next five numbers must end in 5 or 0.
- `t = 6`  -> at most six iterations; it needs both an even digit and a digit divisible by 3.
- `t = 7`  -> at most seven iterations; one of the next seven numbers will end in 7 or 0.
- `t = 8`  -> at most eight iterations; one of the next eight numbers will include a digit 8 or enough even digits.
- `t = 9`  -> at most nine iterations; one of the next nine numbers will include 9 or 0.
- `t = 10` -> at most ten iterations; one of the next ten numbers will include a 0 digit or a 5 plus an even digit.

## Notes

- This solution is simple and straightforward, but not optimized for very large gaps between `n` and the next valid number, but is the best for this particular question as n and t have such small bounds
- For the LeetCode constraints, the brute-force strategy is sufficient.
- Since t is bound between [1,10] and n between [1,100] (2 digits effectively as 100 is returned immediately), the worst case time complexity is O(2*10) = O(20) , which is constant

## Example implementation

```python
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            temp = str(n)
            p = 1
            for i in temp:
                p *= int(i)
            if p % t == 0:
                return n
            n += 1
```
