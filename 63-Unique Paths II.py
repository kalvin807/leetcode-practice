class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        memo = [[0] * n for _ in range(m)]
        
        move = 1
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                move = 0
            memo[i][0] = move 
        move = 1
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                move = 0
            memo[0][i] = move
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 0:
                    memo[i][j] = 0
                else:
                    memo[i][j] = memo[i - 1][j] + memo[i][j - 1]
        return memo[-1][-1]
