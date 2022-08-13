class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = 0, 0
        # pick row
        for i in range(len(matrix)):
            if matrix[i][0] == target or matrix[i][-1] == target:
                return True
            elif matrix[i][0] <= target <= matrix[i][-1]:
                break
        # binary search in that row
        l, r = 0, len(matrix[i]) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if matrix[i][mid] == target:
                return True
            elif matrix[i][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
