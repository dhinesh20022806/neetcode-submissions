class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        seen = set()


        for r in board:
            seen = set()
            for c in r:
                
                if c == ".":
                    continue
                
                if c in seen:
                    return False
                seen.add(c)
        
        for c in range(len(board)):
            seen = set()
            for r in range(len(board)):

                if board[r][c] == ".":
                    continue
                
                if board[r][c] in seen:
                    return False
                seen.add(board[r][c])
        
        def square_valid(fromRow, endRow, fromCol, endCol, board):
            seen = set()
            for i in range(fromRow, endRow):
                for j in range(fromCol, endCol):
                    if board[i][j] == '.':
                        continue
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
            return True
        
        for i in range(0, len(board), 3):   
            for j in range(0, len(board), 3):
                if not square_valid(i, i + 3, j, j + 3, board):
                    return False
        return True

            # 0 - 3, 3 - 6, 6 - 9
            # 0 - 3, 3 - 6, 6 -9



            