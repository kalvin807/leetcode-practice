int_str = ["1","2","3","4","5","6","7","8","9"]
cnt = [0,1,2,3,4,5,6,7,8]
class Solution:
    def solveSudoku(self, board: 'List[List[str]]') -> 'None':
        need_to_fill = []
        for i in cnt:
            for j in cnt:
                if board[i][j] == ".":
                    need_to_fill.append((i, j))   
                    
        def solve(board, need_to_fill):
            if not need_to_fill:
                return True
            i, j = need_to_fill.pop()
            for n in int_str:
                if isSafe(board, i, j, n):
                    board[i][j] = n
                    res = solve(board, need_to_fill)
                    if res:
                        return res
                    board[i][j] = "."
            need_to_fill.append((i , j))
            return False
        
        def isSafe(board, row, col, ch):
            boxrow = row - row % 3
            boxcol = col - col % 3
            if checkrow(board,row,ch) and checkcol(board,col,ch) and checksquare(board,boxrow, boxcol, ch):
                return True
            return False

        def checkrow(board, row, ch):
            for col in cnt:
                if board[row][col] == ch:
                    return False
            return True

        def checkcol(board, col, ch):
            for row in cnt:
                if board[row][col] == ch:
                    return False
            return True

        def checksquare(board, row, col, ch):
            for r in range(row, row+3):
                for c in range(col, col+3):
                    if board[r][c] == ch:
                        return False
            return True

        solve(board, need_to_fill)
