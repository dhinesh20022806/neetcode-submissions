class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        count = 0

                
        def withinrow(row, grid):
            return row < len(grid) and row >= 0
        def withincol(col, grid):
            return col < len(grid[0]) and col >= 0
            

        def dfs(row, col, grid):

            if grid[row][col] == "0" or grid[row][col] == "x":
                return
            
            directions = [( -1, 0), (0, 1), (1, 0), (0, -1)]

            grid[row][col] = "x"

            for i in directions:
                if withinrow(row - i[0], grid) and withincol(col - i[1], grid):
                    dfs(row - i[0], col - i[1], grid)




        for row in range(len(grid)):
            for col in range(len(grid[0])):

                if grid[row][col] == "1":
                    count += 1
                    dfs(row, col, grid)
        


        
        return count
        