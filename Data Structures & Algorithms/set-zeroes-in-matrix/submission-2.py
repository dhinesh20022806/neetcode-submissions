class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        ROWS = len(matrix)
        COLS = len(matrix[0])

        rowZero = False

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matric[0][c] = 0
                    if r > 0:
                        matric[r][0] = 0
                    else:
                        rowZero = True
        
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][0] == 0 or matric[0][c] == 0:
                    matrix[r][c] = 0
        
        if matric[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        
        if rowZero:
            for c in range(COLS):
                matric[0][c] = 0