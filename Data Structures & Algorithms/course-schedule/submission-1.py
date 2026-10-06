class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        grahp = defaultdict(set)
        for i in prerequisites:
            grahp[i[0]].add(i[1])

        
        visited = set()
        print(grahp)

        def dfs(childNode):

            if childNode in visited:
                return False

            if not grahp[childNode]:
                return True
            
            visited.add(childNode)

            for i in grahp[childNode]:
                if not dfs(i):
                    return False

            visited.remove(childNode)
            
            grahp[childNode] = set()
                    
            return True
        
        for i in range(numCourses):
           if not dfs(i):
            return False
        
        return True