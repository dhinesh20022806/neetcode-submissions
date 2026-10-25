from math import inf
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        def isWithInBox(row, col, grid):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        

        def dfs(row, col, grid, visted):
            if not isWithInBox(row, col, grid):
                return inf
            if grid[row][col] == -1:
                return inf
            if grid[row][col] == 0:
                return 0
            
            if (row, col) in visted:
                return inf
            
            visted.add((row, col))
            
            return 1 + min(dfs(row - 1, col, grid, visted), dfs(row + 1, col, grid, visted), dfs(row, col -1, grid, visted), dfs(row, col + 1, grid, visted))
        

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                visted = set()
                if grid[row][col] == 2147483647:
                    grid[row][col] = min(dfs(row, col, grid, visted), grid[row][col])
        


