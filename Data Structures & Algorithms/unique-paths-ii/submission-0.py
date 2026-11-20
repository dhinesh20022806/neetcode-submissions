class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        memo = {}

        def dfs(row, col):
            if row == len(obstacleGrid) - 1 and col == len(obstacleGrid[0]) -1:
                return 1
            if row == len(obstacleGrid) or col == len(obstacleGrid[0]) or obstacleGrid[row][col] == 1:
                return 0
            
            if (row, col) in memo:
                return memo[(row, col)]
            
            memo[(row, col)] = dfs(row + 1, col) + dfs(row, col + 1)

            return memo[(row, col)]
        
        return dfs(0, 0)