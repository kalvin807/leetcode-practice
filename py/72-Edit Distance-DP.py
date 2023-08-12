class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        memo = [[0] * (m + 1) for _ in range(n + 1)]
        
        # Base case: m or n is 0 length
        for i in range(n + 1):
            memo[i][0] = i
        for j in range(m + 1):
            memo[0][j] = j
            
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    memo[i][j] = memo[i - 1][j - 1]
                else:
                    insert = memo[i - 1][j]
                    remove = memo[i][j - 1]
                    replace = memo[i - 1][j - 1]
                    memo[i][j] = 1 + min(insert, remove, replace)
        return memo[-1][-1]
      # Space O(mn)
      # Time O(mn)
