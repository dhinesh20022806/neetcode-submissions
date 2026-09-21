from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        q = deque([])

        def addRoom(r, c):

            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == -1 or (r, c) in visited:
                return
            
            q.append((r, c))
            visited.add((r, c))

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    q.append([row, col])
                    visited.add((row, col))
        
        dist = 0

        while q:

            for _ in range(len(q)):
                row, col = q.popleft()

                grid[row][col] = dist

                addRoom(row + 1, col)
                addRoom(row - 1, col)
                addRoom(row, col + 1)
                addRoom(row, col - 1)

            dist += 1
            

        

