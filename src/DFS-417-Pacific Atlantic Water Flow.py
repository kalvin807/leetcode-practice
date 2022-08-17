directions = ((0, 1),(1,0),(-1,0),(0,-1))
class Solution:
    def pacificAtlantic(self, height: List[List[int]]) -> List[List[int]]:
        M, N = len(height), len(height[0])
        def dfs(cell, seen):
            i, j = cell
            seen.add(cell)
            for di,dj in directions:
                p, q = i + di, j + dj
                if 0 <= p < M and 0 <= q < N and (p, q) not in seen:
                    if height[p][q] >= height[i][j]:
                        dfs((p, q), seen)
        seen_p = set()
        seen_a = set()
        
        for i in range(N):
            dfs((0, i), seen_p)
            dfs((M - 1, i), seen_a)
        
        for i in range(M):
            dfs((i, 0), seen_p)
            dfs((i, N - 1), seen_a)
            
        return list(seen_p & seen_a)
