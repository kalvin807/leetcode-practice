class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        row = [0, 0, 0]
        col = [0, 0, 0]
        lr_diag = 0
        rl_diag = 0
        
        player = 0 # 0 = player A (X), 1 = player B (O)
        # replay the move
        for i ,j in moves:
            val = -1 if player == 0 else 1
            row[i] += val
            col[j] += val
            
            if i == j:
                lr_diag += val
            if i + j == 2:
                rl_diag += val
            
            if abs(row[i]) == 3 or abs(col[j]) == 3 or abs(lr_diag) == 3 or abs(rl_diag) == 3:
                return "A" if player == 0 else "B"
            player = (player + 1) % 2 
            
        return "Pending" if len(moves) != 9 else "Draw"
