class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words_set = set(words)
        
        memo = {}
        def dfs(word):
            if word in memo:
                return memo[word]
            
            if word in words_set:
                memo[word] = True
                return True
            
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                
                if prefix in words_set and suffix in words_set:
                    return True
                if prefix in words_set and dfs(suffix):
                    return True
                if suffix in words_set and dfs(prefix):
                    return True
            memo[word] = False
            return False
        
        
        
        ans = []
        for w in words:
            words_set.remove(w)
            if dfs(w):
                memo[w] = True
                ans.append(w)
            words_set.add(w)
            
        return ans
