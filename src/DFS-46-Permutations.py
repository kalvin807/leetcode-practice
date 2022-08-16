class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, path, ans):
            if not nums:
                ans.append(path)
            else:
                for i, n in enumerate(nums):
                    dfs(nums[:i] + nums[i + 1 :], path + [nums[i]], ans)

        ans = []
        dfs(nums, [], ans)
        return ans
