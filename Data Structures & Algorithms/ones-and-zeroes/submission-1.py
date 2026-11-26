class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        

        def dfs(i, curr, ones, zeros):
            
            if ones > n or zeros > m:
                return 0
            
            if i >= len(strs):
                return len(curr)
            


            currentOne = 0
            currentZero = 0

            for j in range(0, len(strs[i])):
                if strs[i][j] == '0':
                    currentZero += 1
                else:
                    currentOne += 1

            curr.append(strs[i])

            take = dfs(i + 1, curr, ones + currentOne, zeros + currentZero)

            curr.pop()

            skip = dfs(i + 1, curr, ones, zeros)

            return max(take, skip)
        return dfs(0, [], 0, 0)
