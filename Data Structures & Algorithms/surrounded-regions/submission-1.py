class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board) , len(board[0])

        def dfs(r, c):

            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] == 'X' or board[r][c] == '#':
                return
            
            board[r][c] = '#'

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
        

        for row in range(ROWS):
            dfs(row, 0)
            dfs(row, COLS - 1)
        
        for col in range(COLS):
            dfs(0, col)
            dfs(ROWS - 1, col)
        
        
        for row in range(ROWS):
            for col in range(COLS):
                
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                if board[row][col] == '#':
                    board[row][col] = 'O'
        
            