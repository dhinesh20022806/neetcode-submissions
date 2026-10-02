class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_word = False
    
    def addWords(self, word: str):
        
        curr = self

        for c in word:

            if not c in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])

        visited = [[False] * COLS for _ in range(ROWS)]

        root = TrieNode()

        for word in words:
            root.addWords(word)
        
        res = set()

        def dfs(row, col, node, word):

            if row < 0 or row >= ROWS or col < 0 or col >= COLS or visited[row][col] or not board[row][col] in node.children:
                return
            

            word += board[row][col]
            node = node.children[board[row][col]]
            if node.is_word:
                res.add(word)
            

            visited[row][col] = True

            dfs(row - 1, col, node, word)
            dfs(row + 1, col, node, word)
            dfs(row, col - 1, node, word)
            dfs(row, col + 1, node, word)

            visited[row][col] = False
        
        for row in range(ROWS):
            for col in range(COLS):
                dfs(row, col, root, "")
        return list(res)