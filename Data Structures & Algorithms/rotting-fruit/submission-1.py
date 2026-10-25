from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        

        ROWS,COLS = len(grid), len(grid[0])

        q = deque([])

        def addCell(row, col):

            if row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] == 2 or grid[row][col] == 0:
                return

            grid[row][col] = 2
            q.append([row, col])

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    q.append([row, col])
        
        mintues = -1

        if len(q) == 0:
            return 0

        while q:
            print(q)
            for _ in range(len(q)):
                row, col = q.popleft()
                

                addCell(row - 1, col)
                addCell(row + 1, col)
                addCell(row, col - 1)
                addCell(row, col + 1)

            mintues += 1
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    return -1
        
        return mintues
            





