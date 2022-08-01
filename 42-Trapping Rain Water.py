class Solution:
    def trap(self, height: List[int]) -> int:
        water = [0] * len(height)
        # Fill column with water with heigth from L to R
        highest = 0
        for i, h in enumerate(height):
            highest = max(h, highest)
            water[i] = highest
        # Fill column with water with heigth from R to L
        highest = 0
        for i in range(len(height) - 1, -1, -1):
            h = height[i]
            highest = max(h, highest)
            # Current water level is calculated by max water can hold - floor height
            # max water can hold is the shorter wall at L or R
            water[i] = min(water[i], highest) - h
        return sum(water)
