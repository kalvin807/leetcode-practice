class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = [[0] * n for _ in range(m)]
        
        v = 0
        for i in range(m):
            v += grid[i][0]
            memo[i][0] = v
        v = 0
        for i in range(n):
            v += grid[0][i]
            memo[0][i] = v
            
        for i in range(1, m):
            for j in range(1, n):
                memo[i][j] = min(memo[i - 1][j], memo[i][j - 1]) + grid[i][j]
        return memo[-1][-1]
