class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        memo = {}

        def dfs(row, col):            
            if row >= ROWS or col >= COLS:
                return float('inf')

            if (row, col) in memo:
                return memo[(row, col)]
            
            down = dfs(row + 1, col)
            right = dfs(row, col + 1)

            if down == float('inf') and right == float('inf'):
                return grid[row][col]
            
            memo[(row, col)] = grid[row][col] + min(down, right)
            return memo[(row, col)]
        return dfs(0, 0)