from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        q = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)

        order = []
        while q:
            course = q.popleft()
            order.append(course)

            for next_course in graph[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    q.append(next_course)

        return order if len(order) == numCourses else []


# Time: O(numCourses + len(prerequisites))
# Space: O(numCourses + len(prerequisites))
