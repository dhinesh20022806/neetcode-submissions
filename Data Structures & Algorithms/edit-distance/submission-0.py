class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        m, n = len(word1), len(word2)

        memo = {} 

        def dfs(i, j):

            if i == m:

                return n - j
            
            if j == n:
                return m - i

            if (i, j) in memo:
                return memo[(i, j)]

            if word1[i] == word2[j]:
                memo[(i, j)] =  dfs(i + 1, j + 1)
                return memo[(i, j)]
            
            res = dfs(i + 1, j)

            res = min(res, dfs(i + 1, j + 1), dfs(i, j + 1))

            memo[(i, j)] =  1 + res

            return memo[(i, j)]
        
        return dfs(0, 0)


