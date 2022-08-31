class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(set)
        
        for course, prereq in prerequisites:
            graph[course].add(prereq)
            
        takencourses = set()
        for i in range(numCourses):
            self.dfs(i, takencourses, graph, set())
        
        return len(takencourses) == numCourses
   
    def dfs(self, n, takencourses, graph, visited):
        if n in takencourses:
            return True 
        if n in visited:
            return False
        visited.add(n)
        for prereq in graph[n]:
            if not self.dfs(prereq, takencourses, graph, visited):
                return False
        takencourses.add(n)
        visited.remove(n)
        return True
        