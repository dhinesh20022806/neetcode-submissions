class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        visited = set()

        grahp = [[i] for i in range(n)]

        for k, m in edges:

            grahp[k].append(m)
            grahp[m].append(k)

        
        res = 0


        def dfs(i):

            if i in visited:
                return 0

            visited.add(i)

            for node in grahp[i]:
                dfs(node)
            return 1


        for i in range(n):

           result = dfs(i)
           res += result
        

        return res