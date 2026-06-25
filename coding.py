# 2402. Meeting Rooms III
#
# You are given an integer n. There are n meeting rooms numbered from
# 0 to n - 1.
#
# You are also given a 2D integer array meetings, where meetings[i] =
# [start_i, end_i] represents a meeting held during [start_i, end_i).
# All start times are unique.
#
# Meetings are assigned to rooms using these rules:
#   1. Each meeting uses the available room with the smallest number.
#   2. If no room is available, the meeting is delayed until a room
#      becomes free. The delayed meeting keeps its original duration.
#   3. When a room becomes free, the meeting with the earliest original
#      start time gets the room.
#
# Return the number of the room that held the most meetings. If multiple
# rooms held the same number of meetings, return the smallest room number.
#
# Example 1:
# Input: n = 2, meetings = [[0, 10], [1, 5], [2, 7], [3, 4]]
# Output: 0
# Explanation:
#   At time 0, meeting [0, 10] starts in room 0.
#   At time 1, meeting [1, 5] starts in room 1.
#   Meetings [2, 7] and [3, 4] must be delayed.
#   At time 5, meeting [2, 7] starts in room 1 and ends at time 10.
#   At time 10, meeting [3, 4] starts in room 0 and ends at time 11.
#   Both rooms held two meetings, so return room 0.
#
# Example 2:
# Input: n = 3, meetings = [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]
# Output: 1

from typing import List
import heapq


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        available = [i for i in range(n)]
        heapq.heapify(available)
        busy = []
        count = [0] * n
        for start, end in meetings:
            duration = end - start
            while len(busy) and busy[0][0] <=start:
                _, room = heapq.heappop(busy)
                heapq.heappush(available, room)
            if available:
                room = heapq.heappop(available)
                new_end = end
            else:
                earliest_end, room = heapq.heappop(busy)
                new_end = earliest_end + duration
            heapq.heappush(busy,(new_end , room))
            count[room] += 1
        return count.index(max(count))