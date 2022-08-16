import collections

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


class TrieNode:
    def __init__(self, isWord=False):
        self.next = collections.defaultdict(TrieNode)
        self.isWord = isWord
        self.numChild = 0


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        M, N = len(board), len(board[0])
        for w in words:
            node = root
            for c in w:
                node = node.next[c]
                node.numChild += 1
            node.isWord = True

        ans = []

        def dfs(i, j, node, word):
            if node.isWord:
                node.isWord = False
                ans.append(word)
                remove(word)
            temp = board[i][j]
            board[i][j] = "#"
            for di, dj in directions:
                p, q = i + di, j + dj
                if 0 <= p < M and 0 <= q < N and (c := board[p][q]) in node.next:
                    dfs(p, q, node.next[c], word + c)
            board[i][j] = temp

        def remove(word):
            node = root
            stack = []
            for w in word:
                stack.append([node, w])
                node = node.next.get(w)
                if not node:
                    return
            # now node is the leaf node, stack.top is [its parent, and key]
            while stack:
                node, w = stack.pop()
                if node.next[w].numChild == 0:
                    del node.next[w]
                node.numChild -= 1

        for i in range(M):
            for j in range(N):
                if (c := board[i][j]) in root.next:
                    dfs(i, j, root.next[c], c)
        return ans
