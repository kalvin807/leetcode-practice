class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        prev = 2
        prev_prev = 1
        for _ in range(2, n):
            current = prev + prev_prev
            prev, prev_prev = current, prev
        return current
