class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        ROWS = len(matrix)
        COLS = len(matrix[0])

        marks = [[i for i in range(COLS)] for i in range(ROWS)]


        newRow = ROWS - 1

        for row in range(ROWS):
            newRow = newRow - row
            for col in range(COLS):
                marks[col][newRow] = matrix[row][col]
        
        for row in range(ROWS):
            for col in range(COLS):
                matrix[row][col] = marks[row][col]
