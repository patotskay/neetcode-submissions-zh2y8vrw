from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return
        
        queue = deque()
        rows, cols = len(grid), len(grid[0])
        INF = 2147483647
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))

        while queue:

            r, c = queue.popleft()
            
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                di, dj = r + dr, c + dc
                if 0 <= di < rows and 0 <= dj < cols and grid[di][dj] == INF:
                    grid[di][dj] = grid[r][c] + 1
                    queue.append((di, dj))
