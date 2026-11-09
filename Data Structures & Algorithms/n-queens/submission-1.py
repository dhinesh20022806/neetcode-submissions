class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        

        resStr = ''
        res = []

        for _ in range(n):
            for i in range(n):
                if i == len(res):
                    resStr += "Q"
                else:
                    resStr += "."
            res.append(resStr)
            resStr = ""
        
        def isValidRow(queens, c):
            queens_count = 0
            for r in range(len(queens)):
                if queens[r][c] == 'Q':
                    queens_count += 1
            
            
            return False if queens_count > 1 else True

        def isValidRightDiaganal(queens, start):
            queens_count = 0
            for i in range(len(queens) - 1, -1, -1):
                if start >= 0:
                    if queens[i][start] == "Q":
                        queens_count += 1
                    start -= 1
                else:
                    break
            
            return False if queens_count > 1 else True

        def isValidLeftDiaganal(queens, start):
            queens_count = 0
            for i in range(len(queens) - 1, -1, -1):
                if start < len(queens[0]):
                    if queens[i][start] == "Q":
                        queens_count += 1
                else:
                    break
                start += 1
            return False if queens_count > 1 else True

        resQueens = []
        def dfs(queens, index):


            if  not isValidRow(queens, index):
                return

            if not isValidLeftDiaganal(queens, index):
                return

            if not isValidRightDiaganal(queens, index):
                return
            if len(queens) == len(res):
                resQueens.append(queens[:])
                return
      
            for i in range(n):
                queens.append(res[i])
                dfs(queens, i)
                queens.pop()
        dfs([], 0)
        return resQueens