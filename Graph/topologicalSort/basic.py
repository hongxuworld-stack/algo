"""
Topological Sort 拓扑排序

什么时候用:
- 题目里有「先后顺序 / prerequisite / dependency」。
- 比如: 先修 A, 才能修 B。
- 图通常是 directed graph。
- 如果有 cycle, 说明依赖关系互相卡住, 不可能完成。

核心问题:
- 找到一个合法顺序, 让每个 node 都出现在它依赖的东西后面。


1. 边的方向怎么想

LeetCode Course Schedule:
prerequisites = [[cur, pre]]

意思是:
- 想学 cur, 必须先学 pre。

所以边应该是:
pre -> cur

含义:
- pre 学完以后, 可以 unlock cur。

代码:
for cur, pre in prerequisites:
    graph[pre].append(cur)


2. indegree 是什么

如果边是:
pre -> cur

那么:
indegree[cur] = cur 还剩多少个 prerequisite 没完成

也可以理解为:
有多少条边指向 cur。

例子:
prerequisites = [[2, 0], [2, 1], [3, 2]]

意思是:
- 2 需要 0 和 1
- 3 需要 2

图:
0 -> 2
1 -> 2
2 -> 3

indegree:
0: 0
1: 0
2: 2
3: 1

indegree == 0 的 node 可以马上做。


3. BFS / Kahn Algorithm 思路

步骤:
1. 建图: pre -> cur
2. 统计每个 node 的 indegree
3. 把所有 indegree == 0 的 node 放进 queue
4. 每次 pop 一个 node, 表示这个 node 已完成
5. 它指向的 next_node 少了一个 prerequisite:
   indegree[next_node] -= 1
6. 如果 next_node 的 indegree 变成 0, 放进 queue
7. 最后如果处理过所有 node, 说明没有 cycle


4. 为什么能判断 cycle

有 cycle 的时候, cycle 里面的 node 会互相依赖。

例子:
0 -> 1
1 -> 0

indegree:
0: 1
1: 1

没有任何 node 的 indegree 是 0, queue 一开始就是空的。
所以 processed count 不会等于 numCourses。


5. Course Schedule 207

只需要判断能不能完成:
return processed == numCourses

或者:
return all(indegree == 0)


6. Course Schedule 210

需要返回一个具体学习顺序:
- 每次从 queue pop 出来的 node 加入 order
- 如果最后 len(order) == numCourses, return order
- 否则有 cycle, return []


7. 常见坑

不要把方向想反:
graph[cur].append(pre)

这表示 cur -> pre, 也就是「cur 指向它需要的 prerequisite」。
这个方向不是不能做, 但不适合 Kahn BFS 的 unlock 思路。

Kahn BFS 最自然的方向是:
pre -> cur

因为学完 pre 后, 可以直接找到它 unlock 了哪些 cur。


Minimal template:

from collections import defaultdict, deque

graph = defaultdict(list)
indegree = [0] * numCourses

for cur, pre in prerequisites:
    graph[pre].append(cur)
    indegree[cur] += 1

q = deque()
for course in range(numCourses):
    if indegree[course] == 0:
        q.append(course)

processed = 0
while q:
    course = q.popleft()
    processed += 1

    for next_course in graph[course]:
        indegree[next_course] -= 1
        if indegree[next_course] == 0:
            q.append(next_course)

return processed == numCourses
"""
