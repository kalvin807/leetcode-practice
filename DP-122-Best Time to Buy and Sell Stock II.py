class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_hold, cur_not_hold = -float("inf"), 0
        
        for p in prices:
            prev_hold, prev_not_hold = cur_hold, cur_not_hold
            # Everyday if u are holding stock that means
            
            # You Diamond hand or you bought today stock
            cur_hold = max(prev_hold, prev_not_hold - p)
            # Cash is king or you close position
            cur_not_hold = max(prev_not_hold, prev_hold + p)
        
        return cur_not_hold if cur_not_hold >= 0 else 0 
