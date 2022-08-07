class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Memo of in each day
        # The profit when
        # the tnx count is k and if I have position or not
        # Each day will look like [no pos, has pos] * txn count (2 max, so 0, 1, 2) 
        open_2, open_1 = -float("inf"), -float("inf")
        close_2, close_1 = 0, 0
        
        for p in prices:
            prev_open_2, prev_open_1 = open_2, open_1
            prev_close_2, prev_close_1 = close_2, close_1
            
            open_1 = max(prev_open_1, - p)
            open_2 = max(prev_open_2, prev_close_1 - p)
            close_1 = max(prev_close_1, prev_open_1 + p)
            close_2 =  max(prev_close_2, prev_open_2 + p)
        
        return close_2
