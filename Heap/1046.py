# 1046. Last Stone Weight
#
# You are given an array of integers stones, where stones[i] is the
# weight of the ith stone.
#
# On each turn, choose the two heaviest stones and smash them together.
# Suppose their weights are x and y, where x <= y:
#   - If x == y, both stones are destroyed.
#   - If x != y, the stone of weight x is destroyed and the stone of
#     weight y has a new weight of y - x.
#
# Return the weight of the last remaining stone. If no stones remain,
# return 0.
#
# Example 1:
# Input: stones = [2, 7, 4, 1, 8, 1]
# Output: 1
# Explanation:
#   7 and 8 -> 1, stones become [2, 4, 1, 1, 1]
#   2 and 4 -> 2, stones become [2, 1, 1, 1]
#   2 and 1 -> 1, stones become [1, 1, 1]
#   1 and 1 -> 0, stones become [1]
#
# Example 2:
# Input: stones = [1]
# Output: 1

from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        while len(heap) >= 2:
            heaviest = -heapq.heappop(heap)
            second_heaviest = -heapq.heappop(heap)

            if heaviest != second_heaviest:
                new_weight = heaviest - second_heaviest
                heapq.heappush(heap, -new_weight)

        return -heap[0] if heap else 0
