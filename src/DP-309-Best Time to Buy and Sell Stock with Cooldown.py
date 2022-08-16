class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        day = len(prices)
        if day < 2:
            return 0

        memo = [[0] * day, [0] * day]  # memo for not holding and holding
        memo[0][0] = 0  # no position
        memo[1][0] = -prices[0]  # open pos at first day
        memo[0][1] = max(memo[0][0], memo[1][0] + prices[1])
        memo[1][1] = max(memo[1][0], memo[0][0] - prices[1])

        for d in range(2, day):
            # If end of the day, I have no position
            memo[0][d] = max(memo[0][d - 1], memo[1][d - 1] + prices[d])
            # If end of the day, I have some position
            memo[1][d] = max(memo[1][d - 1], memo[0][d - 2] - prices[d])

        return memo[0][-1]
