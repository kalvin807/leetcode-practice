class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        memo = [float("inf")] * len(nums)
        memo[0] = 0  # inital stone no need jump
        n = len(nums)
        for i in range(n):
            if memo[i] == float("inf"):  # unreachable
                continue
            if i + nums[i] >= n - 1:
                return memo[i] + 1  # 1 more jump will reach destination
            for j in range(1, nums[i] + 1):
                memo[i + j] = min(
                    memo[i + j], memo[i] + 1
                )  # Decide if this jump better than previous jump
        return 0
