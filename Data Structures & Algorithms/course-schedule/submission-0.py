class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        grahp = defaultdict(list)


        for i in prerequisites:

            print(i[0], i[1], "pushed")

            grahp[i[0]].append(i[1])

        
        visited = set()

        def dfs(parentNode, childNode):
            if (parentNode, childNode) in visited:
                return False

            visited.add((parentNode, childNode))


            for i in grahp[childNode]:

                if not dfs(childNode, i):
                    return False
            return True
        
        return dfs(-1, 0)