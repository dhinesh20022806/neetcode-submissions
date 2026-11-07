class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        

        res = []


        def dfs(num, curr):
            if len(curr) == k:
                res.append(curr.copy())
                return

            if num > n:
                return
                
            curr.append(num)

            dfs(num + 1, curr)

            curr.pop()

            dfs(num + 1, curr)

        dfs(1, [])

        return res          