class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])


        res = []

        pacific = atlantic = False
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, prevHeight):
            nonlocal pacific, atlantic

            if r < 0 or c < 0:
                pacific = True
                return
            if r >= ROWS or c >= COLS :
                atlantic = True
                return
            
            if heights[r][c] > prevHeight:
                return
            

            tmp = heights[r][c]

            heights[r][c] = float("inf")

            for dx, dy in directions:
                dfs(r + dx, c + dy, tmp)
                if pacific and atlantic:
                    break
            heights[r][c] = tmp
        

        for row in range(ROWS):
            for col in range(COLS):
                pacific = False
                atlantic = False
                dfs(row, col, float('inf'))

                if pacific and atlantic:
                    res.append([row, col])
        return res
        

