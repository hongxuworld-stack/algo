# Given an array of meeting time intervals, where each interval is represented as [start, end], return the minimum number of conference rooms required to hold all meetings.
# If two meetings overlap, they cannot use the same room. If one meeting ends at the same time another meeting starts, they can use the same room.
# Example 1:
# Input: intervals = [[0, 30], [5, 10], [15, 20]]
# Output: 2
# Explanation:
# The meeting [0, 30] overlaps with [5, 10], so we need at least two rooms.
# The meeting [15, 20] can reuse the room from [5, 10], because that meeting has already ended.
# Example 2:
# Input: intervals = [[7, 10], [2, 4]]
# Output: 1
# Explanation:
# The two meetings do not overlap, so only one room is needed.
from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int: