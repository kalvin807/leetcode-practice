import collections
class Solution:
    def numSquares(self, n: int) -> int:
        if not n:
            return 0
        sq_n = [x * x for x in range(1, n + 1) if x * x <= n]

        memo = [float("inf")] * (n + 1)
        memo[0] = 0
        for x in range(1, n + 1):
            for sq_x in sq_n:
                if x - sq_x >= 0:
                    memo[x] = min(memo[x], memo[x - sq_x] + 1)
        return memo[-1]
