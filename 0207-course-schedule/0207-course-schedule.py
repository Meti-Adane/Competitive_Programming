class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = dict()
        takenCourses = set()
        for course, prereq in prerequisites:
            if course not in graph:
                graph[course]= []
            graph[course].append(prereq)
        
        
        def hasCycle(node, visited):
            if node in visited:
                return True
            if node not in graph or node in takenCourses:
                return False
            visited.add(node)
            for prereq in graph[node]:
                if hasCycle(prereq, visited):
                    return True
            takenCourses.add(node)
            visited.remove(node)
            return False
                
        for course in graph:
            if hasCycle(course, set()):
                return False
        return True