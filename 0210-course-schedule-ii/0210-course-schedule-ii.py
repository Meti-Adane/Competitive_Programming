#10:28
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses, prereqs = defaultdict(set), defaultdict(list)
        que = deque()
        course_order = []
        
        for course, prereq in prerequisites:
            courses[course].add(prereq)
            prereqs[prereq].append(course)
        
        for i in range(numCourses):
            if len(courses[i]) == 0:
                que.append(i)
        
        while que:
            course = que.popleft()
            course_order.append(course)
            for d in prereqs[course]:
                courses[d].remove(course)
                if len(courses[d]) == 0:
                    que.append(d)
        if len(course_order) != numCourses:
            return []
        return course_order