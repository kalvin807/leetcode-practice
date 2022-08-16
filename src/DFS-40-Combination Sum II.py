import collections


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        counter = collections.Counter(candidates)
        combo = set()
        self.dfs(target, combo, counter, [])
        return combo

    def dfs(self, target, combo, counter, path):
        if target == 0:
            combo.add(tuple(sorted(path)))

        for k, v in counter.items():
            if v > 0 and k <= target:
                counter[k] -= 1
                path.append(k)
                self.dfs(target - k, combo, counter, path)
                counter[k] += 1
                path.pop()
