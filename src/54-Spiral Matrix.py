# R -> D -> L -> U
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        path = []
        v, h = len(matrix), len(matrix[0])
        step = len(matrix) * len(matrix[0])
        type = 0

        i, j = 0, 0
        v_progress = v
        h_progress = h
        while step > 0:
            # add to path
            path.append(matrix[i][j])
            # update progress
            if type % 2 == 0:
                h_progress -= 1
                if h_progress == 0:
                    type = (type + 1) % 4
                    v -= 1
                    v_progress = v
            else:
                v_progress -= 1
                if v_progress == 0:
                    type = (type + 1) % 4
                    h -= 1
                    h_progress = h
            step -= 1
            i, j = i + directions[type][0], j + directions[type][1]
        return path
