directions = ((1, 0), (-1, 0), (0, 1), (0, -1))


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        largest = -float("inf")
        # Walk over an island and return the size
        # It also remove the island so that it won't get scanned again
        def walk(start):
            island_size = 0
            queue = [start]
            while len(queue):
                x, y = queue.pop()
                grid[x][y] = 3
                island_size += 1
                # walk next
                for dx, dy in directions:
                    p, q = x + dx, y + dy
                    # walk valid cell only
                    if 0 <= p < len(grid) and 0 <= q < len(grid[0]) and grid[p][q] == 1:
                        # Mark it as there is more than 1 way to reach a grid
                        grid[p][q] = 3
                        queue.append((p, q))
                # remove walked cell
            return island_size

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    size = walk((i, j))
                    largest = max(size, largest)

        # No island if the largest is still -ve inf
        return largest if largest != -float("inf") else 0
