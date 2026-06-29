from collections import defaultdict, deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        q = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)

        visited = 0
        while q:
            course = q.popleft()
            visited += 1

            for next_course in graph[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    q.append(next_course)

        return visited == numCourses

class Solution:
    def canFinishDfs(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[pre].append(course)
        # 0 not visited
        # 1 visiting
        # 2 visited
        state = [0] * numCourses
        # dfs represent 有没有环
        def dfs(course):
            if state[course] == 1:
                return True
            if state[course] == 2:
                return False
            state[course]  = 1
            for next_course in graph[course]:
                if dfs(next_course):
                    return True
            state[course] = 2
            return False
        
        for course in range(numCourses):
            if dfs(course):
                return False
        return True
            
            

# Time: O(numCourses + len(prerequisites))
# Space: O(numCourses + len(prerequisites))