import collections

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Step1 Store location of every rotten orange
            # Also store number of good orange
        queue = collections.deque()
        survivor = 0
        
        for i, r in enumerate(grid):
            for j in range(len(r)):
                cell = grid[i][j]
                if cell == 1: # survivor
                    survivor += 1
                if cell == 2:
                    queue.append((i , j))
        
        direction = ((1, 0), (-1, 0), (0, 1), (0, -1))
        time = 0
        # Step2 Iterate the spread until there is no good orange left
            # Each loop = 1 min

        while survivor and len(queue):
            next_wave = collections.deque()
            while len(queue):
                i, j = queue.popleft()
                # Try spread
                for dx, dy in direction:
                    p, q = i + dx, j + dy
                    # Skip illegal pos
                    if not 0 <= p < len(grid):
                        continue
                    if not 0 <= q < len(grid[p]):
                        continue
                    # Skip empty or already rotten
                    if grid[p][q] != 1:
                        continue
                    # Convert to rotten and push to queue
                    grid[p][q] = 2
                    next_wave.append((p, q))
                    survivor -= 1
            time += 1
            queue = next_wave
                       
        # Return the required time
        return time if not survivor else -1 
