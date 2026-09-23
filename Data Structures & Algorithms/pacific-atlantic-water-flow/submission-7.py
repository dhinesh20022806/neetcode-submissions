class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        ROWS, COLS = len(heights), len(heights[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        pacific = [[False] * COLS for _ in range(ROWS)]
        atlantic = [[False] * COLS for _ in range(ROWS)]



        def bfs(source, ocean):

            q = deque(source)

            while q:

                row, col = q.popleft()

                ocean[row][col] = True
                for dx, dy in directions:

                    nx, ny = row + dx, col + dy

                    if 0 <= nx < ROWS and 0 <= ny < COLS and not ocean[nx][ny] and heights[nx][ny] >= heights[row][col]:
                        q.append((nx, ny))


        pac = []
        atl = []

        for row in range(ROWS):
            pac.append((row, 0))
            atl.append((row, COLS - 1))
        
        for col in range(COLS):
            pac.append((0, col))
            atl.append((ROWS - 1, col))
        
        bfs(pac, pacific)
        bfs(atl, atlantic)

        res = []

        for row in range(ROWS):
            for col in range(COLS):
                if pacific[row][col] and atlantic[row][col]:
                    res.append([row, col])
        
        return res

        

