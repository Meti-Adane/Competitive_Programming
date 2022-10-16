class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses, prereqs = defaultdict(set), defaultdict(list)
        que = deque()
        takencourses = 0
        for course, prereq in prerequisites:
            courses[course].add(prereq)
            prereqs[prereq].append(course)
        
        for i in range(numCourses):
            if not len(courses[i]):
                que.append(i)
        
        
        while que:
            course = que.popleft()
            takencourses += 1
            for dependant in prereqs[course]:
                courses[dependant].remove(course)
                if not len(courses[dependant]):
                    que.append(dependant)
        return takencourses == numCourses