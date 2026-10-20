class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        

        matrix = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(len(matrix[0])):
            matrix[0][i] = 1
        
        for i in range(len(matrix)):
            matrix[i][0] = 1
        

        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[row])):
                matrix[row][col] = matrix[row - 1][col] + matrix[row][col -1]
        
        return matrix[-1][-1]
