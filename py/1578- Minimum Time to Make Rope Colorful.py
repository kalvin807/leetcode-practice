class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        # at each same color segment, keep only 1 ballon
        # because we can only keep 1, keep the most expensive one to minimise cost.
        i = 0
        total_cost = 0
        while i < len(colors):
            current_color = colors[i]
            window_total_cost = 0
            window_max_cost = 0
            while i < len(colors) and colors[i] == current_color:
                window_total_cost += neededTime[i]
                window_max_cost = max(window_max_cost, neededTime[i])
                i += 1
            total_cost += window_total_cost - window_max_cost
        return total_cost
            
