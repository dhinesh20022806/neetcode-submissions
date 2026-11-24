class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])


        memo = {}
        def dfs(prev, row, col):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or prev >= matrix[row][col]:
                return 0
            
            if (row, col) in memo:
                return memo[(row, col)]

            # dic = [(0, 1), (-1, 0), (1, 0), (0, -1)]
            current_value = matrix[row][col]

            memo[(row, col)] = 1 + max(dfs(current_value, row - 1, col),
                          dfs(current_value, row + 1, col), 
                          dfs(current_value, row, col - 1), 
                          dfs(current_value, row, col + 1))
            return memo[(row, col)]
        
        res = 0
        for row in range(ROWS):
            for col in range(COLS):
               res = max(res, dfs(float("-inf"), row, col))

        return res 

