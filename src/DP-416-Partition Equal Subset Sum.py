class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        # End case 1: sum cannot split into two
        if total % 2 != 0:
            return False
        total = total // 2
        n = len(nums)
        memo = [[False] * (total + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            memo[i][0] = True  #
        for i in range(1, n + 1, 1):
            for j in range(1, total + 1, 1):
                memo[i][j] = memo[i - 1][j]
                if j - nums[i - 1] >= 0:
                    memo[i][j] = memo[i][j] or memo[i - 1][j - nums[i - 1]]

        return memo[n][total]

    # time complexity = O(n^2)
    # space complexity = O(n^2)
