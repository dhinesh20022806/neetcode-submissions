class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        memo = {}


        def dfs(s1, s2, i, j):
            if i >= len(s1) or j >= len(s2):
                return 0
            

            if (i , j) in memo:
                return memo[(i, j)]

            if s1[i] == s2[j]:
                return 1 + dfs(s1, s2, i + 1, j + 1)
            
            memo[(i, j)] = max(dfs(s1, s2, i + 1, j), dfs(s1, s2, i, j + 1))

            return memo[(i, j)]

        return dfs(text1, text2, 0, 0)