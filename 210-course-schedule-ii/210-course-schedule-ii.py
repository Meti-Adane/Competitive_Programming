#4:45
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        taken = [False for _ in range(numCourses)]
        visited = [False for _ in range(numCourses)]
        graph = defaultdict(list)
        ans = []
        
        for a, b in prerequisites:
            graph[a].append(b)
          
        
        
        def canTakeClass(n):
            if taken[n]:
                return True
            if visited[n]:
                return False
            visited[n] = True
            
            for prereq in graph[n]:
                if not canTakeClass(prereq):
                    return False
            taken[n] = True
            visited[n] = False
            ans.append(n)
            return True
        
        for i in range(numCourses):
            if not canTakeClass(i):
                return []
        return ans
        