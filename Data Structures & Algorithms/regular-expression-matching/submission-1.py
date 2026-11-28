class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        memo = {}

        def dfs(i, j):

            if i == len(s) and j == len(p):
                return True

            if (i, j) in memo:
                return memo[(i, j)]

            if i < len(s) and j < len(p) and  p[j] == ".":
               if dfs(i + 1, j + 1):
                    return True

            if i < len(s) and j < len(p) and p[j] == "*":
                if dfs(i + 1, j + 1) or dfs(i + 1, j):
                    return True
            
            if j < len(p) and i < len(s) and s[i] == p[j]:
                if dfs(i + 1, j + 1):
                    return True
            
            memo[(i,j)] = False

            return False
        return dfs(0, 0)