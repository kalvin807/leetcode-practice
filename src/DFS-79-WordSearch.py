directions = ((1, 0), (-1, 0), (0, 1), (0, -1))


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M, N = len(board), len(board[0])
        word_len = len(word) - 1

        def dfs(cell, word_idx, history):
            i, j = cell
            # Exit 1: cell un-match
            if board[i][j] != word[word_idx]:
                return False
            # Exit 2: word fully matched
            if board[i][j] == word[word_idx] and word_idx == word_len:
                found = True
                return True
            # Go next cell
            history.add(cell)
            for dy, dx in directions:
                y, x = i + dy, j + dx
                if (
                    0 <= y < M
                    and 0 <= x < N
                    and not (y, x) in history
                    and word_idx + 1 <= word_len
                ):
                    # Reduce copy as much as possible
                    if dfs((y, x), word_idx + 1, history):
                        return True
            history.remove(cell)
            return False

        # Try every cell
        for i in range(M):
            for j in range(N):
                if dfs((i, j), 0, set()):
                    return True
        return False


# Time compexity = O(N ^ 2)
# Space compexity = O(N ^ 2)
# Interesting read on why class attribute is slow in Python
# https://stackoverflow.com/questions/28597014/python-why-is-accessing-instance-attribute-slower-than-local
# https://docs.python.org/3/tutorial/classes.html
