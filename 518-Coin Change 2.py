class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = [[0] * (amount + 1)] * (len(coins) + 1)
        for i in range(len(memo)):
            memo[i][0] = 1
        
        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                memo[i][j] = memo[i - 1][j]
                if (remain := j - coins[i - 1]) >= 0:
                    memo[i][j] += memo[i][remain]
        return memo[-1][-1]
