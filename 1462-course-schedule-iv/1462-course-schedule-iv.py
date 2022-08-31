#5:34
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        graph = defaultdict(set)
        answer = []
        visited = set()
        for a, b in prerequisites:
            graph[b].add(a)
            
        def compress(course):
            if course in visited:
                return 
            prereqs = set()
            visited.add(course)
            for p in graph[course]:
                compress(p)
                prereqs.update(graph[p])
            graph[course].update(prereqs)
            
        for i in range(numCourses):
            compress(i)
            
        for i, j in queries:
            answer.append(i in graph[j])
        return answer

  