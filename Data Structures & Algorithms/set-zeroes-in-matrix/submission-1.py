class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        ROWS = len(matrix)
        COLS = len(matrix[0])

        rowMarks = [False for i in range(ROWS)]
        colMarks = [False for i in range(COLS)]

        for row in range(ROWS):
            for col in range(COLS):

                if matrix[row][col] == 0:
                    rowMarks[row] = True
                    colMarks[col] = True
        
        for row in range(ROWS):
            for col in range(COLS):

                if rowMarks[row] or colMarks[col]:
                    matrix[row][col] = 0
        