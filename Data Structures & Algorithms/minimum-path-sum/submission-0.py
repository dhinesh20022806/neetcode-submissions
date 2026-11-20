class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(row, col):            
            if row >= ROWS or col >= COLS:
                return float('inf')
            
            down = dfs(row + 1, col)
            right = dfs(row, col + 1)

            if down == float('inf') and right == float('inf'):
                return grid[row][col]
            
            return grid[row][col] + min(down, right)
        
        return dfs(0, 0)