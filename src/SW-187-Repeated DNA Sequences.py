class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []

        seens = set()
        repeated = set()

        for i in range(len(s) - 9):
            sub = s[i : i + 10]
            if sub in seens:
                repeated.add(sub)
            else:
                seens.add(sub)
        return list(repeated)
