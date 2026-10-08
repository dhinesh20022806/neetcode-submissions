class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses

        adj = [[] for _ in range(numCourses)]


        for src, dst in prerequisites:
            indegree[src] += 1
            adj[dst].append(src)
        
        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        finished_list = []

        finish = 0

        while q:
            node = q.popleft()
            finish += 1
            finished_list.append(node)

            for nei in adj[node]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)
        
        return finished_list if finish == numCourses else []
