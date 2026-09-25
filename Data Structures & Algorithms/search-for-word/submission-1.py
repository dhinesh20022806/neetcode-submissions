class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        isExists = False

        visited = [[False] * COLS for _ in range(ROWS)]


        def dfs(i, row, col, word, board):
            nonlocal isExists, visited

            if i >= len(word):
                isExists = True
                return

            if row < 0 or col < 0 or row >= ROWS or col >= COLS or visited[row][col]:
                return
            
            
            
            if word[i] != board[row][col]:
                return
            
          

            visited[row][col] = True

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dx, dy in directions:
                dfs(i + 1, row + dx, col + dy, word, board)
                if isExists:
                    return
            
            visited[row][col] = False
        
        for row in range(ROWS):
            for col in range(COLS):
                dfs(0, row, col, word, board)
                if isExists:
                    return isExists


        return isExists