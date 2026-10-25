class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS,COLS = len(board), len(board[0])

        res = []
        vistied = [[False] * COLS for _ in range(ROWS)]

        def dfs(row, col, i, word):
            nonlocal board

            # if word == "bat":
            #     print(row, col, i, word[i], board[row][col], vistied[row][col])

            
            if row >= ROWS or row < 0 or col >= COLS or col < 0 or vistied[row][col] or word[i] != board[row][col]:
                return False
            

            if i >= len(word) - 1:
                return True
            
            vistied[row][col] = True

            direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for dx, dy in direction:
                if dfs(row + dx, col + dy, i + 1, word):
                    vistied[row][col] = False
                    return True
            
            vistied[row][col] = False

            return False

        for word in words:
            is_exists = False
            for row in range(ROWS):
                for col in range(COLS):
                    if board[row][col] == word[0]:
                        if dfs(row, col, 0, word):
                            is_exists = True
                            res.append(word)
                    if is_exists:
                        break
                if is_exists:
                    break
        
        return res


