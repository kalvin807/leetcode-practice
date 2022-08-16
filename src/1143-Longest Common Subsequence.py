class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
    
        for i in range(len(text1)):
            for j in range(len(text2)):
                p, q = i + 1, j + 1
                if text1[i] == text2[j]:
                    memo[p][q] = 1 + memo[i][j] # extend the common char count
                else:
                    memo[p][q] = max(memo[p - 1][q], memo[p][q - 1]) # prop
        return memo[-1][-1]
