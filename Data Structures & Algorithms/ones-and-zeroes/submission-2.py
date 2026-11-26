class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        memo = {}


        def dfs(i, ones, zeros):
            
            if i == len(strs):
                return 0

            if (i, ones, zeros) in memo:
                return memo[(i, ones, zeros)]
            
            memo[(i, ones, zeros)] = dfs(i + 1, ones, zeros)

            currentOne = 0
            currentZero = 0

            for j in range(0, len(strs[i])):
                if strs[i][j] == '0':
                    currentZero += 1
                else:
                    currentOne += 1


            if currentOne <= ones and currentZero <= zeros:
                memo[(i, ones, zeros)] = max(memo[(i, ones, zeros)], 1 + dfs(i + 1,  ones - currentOne, zeros - currentZero))

            return memo[(i, ones, zeros)]

        return dfs(0, n, m)
