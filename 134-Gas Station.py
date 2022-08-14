class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        fuel_now = 0
        fuel_net = 0
        start_at = 0
        
        for i, (g, c) in enumerate(zip(gas, cost)):
            fuel_now += g - c # current trip
            fuel_net += g - c # total consumption 

            # If fuel here is zero
            # -> there is not enough gas to reach next station
            # -> all station from start_at to i are not able to make it
            # -> as to each one station ur fuel must not < 0
            # We move the starting point to next station
            if fuel_now < 0:
                start_at = i + 1
                fuel_now = 0
            
        # The trip only possible if the net consumption is larger or equal to zero. zero = just enough
        return start_at if fuel_net >= 0 else -1
