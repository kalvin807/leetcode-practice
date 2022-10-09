class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = dict()
        def recur_minDistance(i, j):
            # end cases
            if i == len(word1) and j == len(word2):
                return 0
            if i == len(word1):
                return len(word2) - j # Insert remaining char
            if j == len(word2):
                return len(word1) - i # Delete remaining char

            if (i,j) not in memo:
                if word1[i] == word2[j]:
                    # Go to next char without edit
                    ans = recur_minDistance(i + 1, j + 1)
                else:
                    insert = 1 + recur_minDistance(i, j + 1)
                    delete = 1 + recur_minDistance(i + 1, j)
                    replace = 1 + recur_minDistance(i + 1, j + 1)
                    ans = min(insert, delete, replace)
                memo[(i, j)] = ans
            return memo[(i, j)]
        return recur_minDistance(0, 0)

 # Space O(mn)
 # Time O(mn) with cache, every combo only run once
     
    
    
