class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        val = 1
        hole = n * n
        i, j = 0, 0
        di, dj = 0, 1
        while hole:
            matrix[i][j] = val
            if not(0 <= i + di < n and 0 <= j + dj < n and matrix[i + di][j + dj] == 0):
                di, dj = dj, -di  # 0, 1 -> 1, 0 -> 0, -1 -> -1, 0 -> 0, 1
            i, j = i + di, j + dj
            hole -= 1
            val += 1
        return matrix
