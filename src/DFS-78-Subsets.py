class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        self.dfs(nums, [], ans)
        return ans

    def dfs(self, ns, path, ans):
        ans.add(tuple(sorted(path)))
        for i, n in enumerate(ns):
            self.dfs(ns[i + 1 :], path + [n], ans)
