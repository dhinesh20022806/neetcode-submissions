class TrieNode:
    def __init__(self, row, col ):
        self.children = {}
        self.is_word = False
        self.row = row
        self.col = col

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS,COLS = len(board), len(board[0])

        res = []
        vistied = [[False] * COLS for _ in range(ROWS)]

        curr = TrieNode(0, 0)

        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(row, col, i, word, curr):
            nonlocal board

            if row >= ROWS or row < 0 or col >= COLS or col < 0 or vistied[row][col] or word[i] != board[row][col]:
                return False

            vistied[row][col] = True

            print(curr.children, word, i)
            if not word[i] in curr.children:
                curr.children[word[i]] = TrieNode(row, col)
            
            curr = curr.children[word[i]]


            if i >= len(word) - 1:
                return True
            
         
            for dx, dy in direction:
                if dfs(row + dx, col + dy, i + 1, word, curr):
                    vistied[row][col] = False
                    return True
            
            vistied[row][col] = False

            return False
        
        temp = curr

        for word in words:
            is_exists = False
            curr = temp
            if word[0] in curr.children:
                curr = curr.children[word[0]]
                for i in range(1, len(word)):
                    if not word[i] in curr.children:
                        for dx, dy in direction:
                            if dfs(curr.row + dx, curr.col + dy, i, word, curr):
                                is_exists = True
                                res.append(word)
                    
                                break
                    if is_exists:
                        break    
                    print(i, word, curr.children)
                    curr = curr.children[word[i]]
            
            if is_exists:
                continue

            for row in range(ROWS):
                for col in range(COLS):
                    if board[row][col] == word[0]:
                        if dfs(row, col, 0, word, curr):
                            is_exists = True
                            res.append(word)
                    if is_exists:
                        break
                if is_exists:
                    break        
        return res


