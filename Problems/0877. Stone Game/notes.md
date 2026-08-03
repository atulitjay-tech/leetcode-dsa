# Stone Game (LeetCode 877)

The `main.py` implementation always returns `True`:

```python
class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        return True
```

## Why this is valid for LeetCode 877

- In this problem, Alice and Bob play optimally and Alice always goes first.
- The problem guarantees that Alice can always win when both players play optimally.
- Therefore, the answer is always `True` no matter what the pile values are.

## Why this is an optimal solution

- This solution has constant time and constant space: O(1) time, O(1) space.
- It directly returns the correct result for every valid input under the problem constraints.
- On LeetCode 877, this is the simplest correct implementation.

## Important note

- This is a special-case solution that relies on the problem's guarantee.
- It is not a general algorithm for arbitrary two-player stone-taking games.
- For this specific LeetCode question, however, returning `True` is enough.
