class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        dp = [[float('inf') for _ in range(COLS + 1)] for _ in range(ROWS + 1)]

        dp[ROWS - 1][COLS - 1] = grid[ROWS - 1][COLS - 1]

        for row in range(ROWS - 1, -1, -1):
            for col in range(COLS -1, -1, -1):

                minPath = min(dp[row + 1][col], dp[row][col + 1])

                if minPath == float('inf'):
                    dp[row][col] = grid[row][col]
                else:
                    dp[row][col] = grid[row][col] + minPath
        return dp[0][0]