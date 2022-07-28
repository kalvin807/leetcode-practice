class Solution:
    def firstUniqChar(self, s: str) -> int:
        uniq_dict = {}
        for i, c in enumerate(list(s)):
            if not c in uniq_dict:
                uniq_dict[c] = i
            else:
                uniq_dict[c] = -1
        first = float("inf")
        for k, v in uniq_dict.items():
            if v >= 0:
                first = min(v, first)
        return first if first != float("inf") else -1
