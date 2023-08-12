class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        self.dfs(range(1, n + 1), [], k, ans)
        return ans

    def dfs(self, ns, path, k, ans):
        if len(path) == k:
            ans.append(path)
        for i, n in enumerate(ns):
            self.dfs(ns[i + 1 :], path + [n], k, ans)
