from math import inf
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        visit = [[False for _ in range(len(grid[0]))] for _ in range(len(grid)) ]

        def isWithInBox(row, col, grid):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        

        def dfs(row, col, grid):
            if not isWithInBox(row, col, grid):
                return inf
            if grid[row][col] == -1:
                return inf
            if grid[row][col] == 0:
                return 0
            
            if visit[row][col]:
                return inf
            
            visit[row][col] = True
            
            res =  1 + min(dfs(row - 1, col, grid), dfs(row + 1, col, grid), dfs(row, col -1, grid), dfs(row, col + 1, grid))
            
            visit[row][col] = False

            return res
        

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2147483647:
                    grid[row][col] = min(dfs(row, col, grid), grid[row][col])

