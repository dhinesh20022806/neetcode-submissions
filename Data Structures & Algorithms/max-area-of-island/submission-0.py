class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def withinMatrix(row, col, grid):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        max_area = 0

        def dfs(row, col, grid):

            if grid[row][col] == 0 or grid[row][col] == 2:
                return 0
            

            grid[row][col] = 2
            count = 0

            direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for d in direction:

                r = row - d[0]
                c = col - d[1]

                if withinMatrix(r, c, grid):
                    count += dfs(r, c, grid)
            
            return 1 + count
            
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                max_area = max(max_area, dfs(row, col, grid))
        
        return max_area
        