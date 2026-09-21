class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        sumofIsland = 0

        def isInBox(r, c, grid):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        


        def dfs(row, col, grid):

            if not isInBox(row, col, grid):
                return 1
            if grid[row][col] == 0:
                return 1
            if grid[row][col] == 2:
                return 0
            
            grid[row][col] = 2

            
            return dfs(row - 1, col, grid) + dfs(row + 1, col, grid) + dfs(row, col + 1, grid) + dfs(row, col - 1, grid)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                   sumofIsland += dfs(row, col, grid)
        
        return sumofIsland