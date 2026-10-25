class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        grahp = {i: { "indegree": 0, "dep" : set()} for i in range(numCourses)}

        for curr, dep in prerequisites:

            grahp[curr]["dep"].add(dep)
            grahp[curr]["indegree"] += 1

        queue = deque([])

        finished_course = 0

        for i in range(numCourses):
            if grahp[i]["indegree"] == 0:
                queue.append(i)
                del grahp[i]
                finished_course += 1
        
        while queue:
            completed_course = queue.popleft()
            for i in range(numCourses):
                if not grahp.get(i):
                    continue
                if completed_course in  grahp[i]['dep']:
                    grahp[i]['dep'].remove(completed_course)
                    grahp[i]["indegree"] -= 1
                
                if grahp[i]["indegree"] == 0:
                    queue.append(i)
                    finished_course += 1
                    del grahp[i]
        
        return finished_course == numCourses
            




