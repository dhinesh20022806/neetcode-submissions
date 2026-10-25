class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        marks = [ [matrix[r][c] for c in range(COLS)] for r in range(ROWS)]


        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:

                    for mr in range(ROWS):
                        marks[mr][c] = 0
                    for mc in range(COLS):
                        marks[r][mc] = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                matrix[r][c] = marks[r][c] 