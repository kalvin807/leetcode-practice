class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [0] * (amount + 1)
        
        for i in range(1, amount + 1, 1): # money = 0 need no coin
            leastCoin = float('inf')
            for c in coins:
                if (remain := i - c) >= 0:
                    leastCoin = min(leastCoin, memo[remain] + 1)
            memo[i] = leastCoin

        return amt if (amt := memo[amount]) != float('inf') else -1
