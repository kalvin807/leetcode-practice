import string
import collections


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        alphabets = string.ascii_lowercase
        queue = collections.deque([beginWord])
        cnt = 1
        wordSet = set(wordList)
        # BFS
        N = len(queue)
        while N:
            # Loop all word in same layer
            for _ in range(N):
                word = queue.popleft()
                if word == endWord:
                    return cnt
                else:
                    # Try change each char in the work 1 at a time
                    # If the new word is in the wordList
                    # It is a valid next step -> put into queue
                    for i in range(len(word)):
                        for c in alphabets:
                            new_word = word[:i] + c + word[i + 1 :]
                            if new_word in wordSet:
                                wordSet.remove(new_word)
                                queue.append(new_word)
            N = len(queue)
            cnt += 1
        # If the program escape the loop -> BFS cannot find the path -> no such seq exist
        return 0
