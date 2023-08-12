int_str = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
cnt = [0, 1, 2, 3, 4, 5, 6, 7, 8]


class Solution:
    def solveSudoku(self, board: "List[List[str]]") -> "None":
        rows, cols, boxes = defaultdict(set), defaultdict(set), defaultdict(set)
        q = []

        for r in cnt:
            for c in cnt:
                if (v := board[r][c]) == ".":
                    q.append((r, c))
                else:
                    rows[r].add(v)
                    cols[c].add(v)
                    boxes[(r // 3, c // 3)].add(v)

        def dfs():
            if not q:
                return True
            r, c = q.pop()
            b = (r // 3, c // 3)
            for v in int_str:
                if v not in rows[r] and v not in cols[c] and v not in boxes[b]:
                    board[r][c] = v
                    rows[r].add(v)
                    cols[c].add(v)
                    boxes[b].add(v)
                    if dfs():
                        return True
                    board[r][c] = "."
                    rows[r].discard(v)
                    cols[c].discard(v)
                    boxes[b].discard(v)
            q.append((r, c))
            return False

        dfs()
