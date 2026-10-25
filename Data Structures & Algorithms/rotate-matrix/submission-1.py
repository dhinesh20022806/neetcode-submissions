class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        ROWS = len(matrix)
        COLS = len(matrix[0])

        marks = [[0 for i in range(COLS)] for r in range(ROWS)]


        newRow = ROWS 

        for row in range(ROWS):
            newRow = newRow - 1
            print(marks, newRow)
            for col in range(COLS):
                marks[col][newRow] = matrix[row][col]
        print(marks)
        
        for row in range(ROWS):
            for col in range(COLS):
                matrix[row][col] = marks[row][col]
