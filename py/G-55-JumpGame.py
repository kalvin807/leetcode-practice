class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_step = 0  # Current max_step u can go, init will be at first idx
        for i in range(len(nums)):
            if i <= max_step:  # if current tile within max_range
                max_step = max(max_step, i + nums[i])  # Try jump furthest
        return max_step >= len(nums) - 1
