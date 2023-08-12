class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxArea = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            maxArea = max(maxArea, area)
            # Tweak pointer
            # Always try to keep the taller one
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return maxArea
