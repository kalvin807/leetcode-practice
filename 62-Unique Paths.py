class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0] * n for _ in range(m)] # start point, upper left
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0: # on edge, robot can only come from 1 direction
                    memo[i][j] = 1
                else:
                    memo[i][j] = memo[i - 1][j] + memo[i][j - 1] # from top + from left

        return memo[-1][-1] # end point, bottom right
