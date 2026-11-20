class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        if len(obstacleGrid) == 0 or obstacleGrid[0][0] == 1:
            return 0
        dp = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]


        isObstacleExists = False
        for row in range(len(obstacleGrid)):

            if isObstacleExists:
                dp[row][0] = 0
            else:
                if obstacleGrid[row][0] == 0:
                    dp[row][0] = 1
                else:
                    isObstacleExists = True
                    dp[row][0] = 0
        
        isObstacleExists = False

        for col in range(len(obstacleGrid[0])):


            if isObstacleExists:
                dp[0][col] = 0
            else:
                if obstacleGrid[0][col] == 0:
                    dp[0][col] = 1
                else:
                    isObstacleExists = True
                    dp[0][col] = 0
        
        for row in range(1, len(obstacleGrid)):
            for col in range(1, len(obstacleGrid[0])):

                if obstacleGrid[row][col] == 1:
                    dp[row][col] = 0
                    continue
                
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
        
    
        return dp[-1][-1]