class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        memo = {}

        def dfs(i, res):

            if res == t:
                return 1
            if i == len(s):
                return 0
            
            if (i, res) in memo:
                return memo[(i, res)]
            
            memo[(i, res)] = dfs(i + 1, res + s[i]) + dfs(i + 1, res)

            return memo[(i, res)]
        
        return dfs(0, "")