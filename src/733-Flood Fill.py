class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1)) 
        src = image[sr][sc]
        if src == color:
            return image
        
        queue = deque([(sr, sc)])
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if image[r][c] != src:
                    continue
                image[r][c] = color
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(image) and 0 <= nc < len(image[0]):
                        queue.append((nr, nc))          
        return image
