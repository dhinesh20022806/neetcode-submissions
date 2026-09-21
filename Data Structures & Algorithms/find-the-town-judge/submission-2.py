class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        indegree = {}
        outdegree = {}

        for i in range(n + 1):
            indegree[i] = 0
            outdegree[i] = 0


        for row in range(len(trust)):
            indegree[trust[row][0]] = indegree.get(trust[row][0], 0) + 1
            outdegree[trust[row][1]] = outdegree.get(trust[row][1], 0) + 1
        
        print(indegree, outdegree)

        for i,(k, v) in enumerate(indegree.items()):

            if v == 0 and outdegree.get(k) and outdegree.get(k) == n - 1:
                return k
        
        return -1

