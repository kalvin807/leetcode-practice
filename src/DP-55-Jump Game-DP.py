class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = [False] * len(nums)
        memo[0] = True  # First stone is always reachable

        for i in range(len(nums)):
            if memo[i] is False:
                continue
            if i + nums[i] >= len(nums) - 1:
                return True
            for j in range(1, nums[i] + 1, 1):  # Reachable stones
                memo[i + j] = True
        return False

    # Time complexity O(n^2)
