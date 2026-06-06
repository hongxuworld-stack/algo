import heapq

class MedianFinder:

    def __init__(self):
        self.left = []   # max heap, smaller half
        self.right = []  # min heap, larger half

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)

        # 保证 left 里的最大值 <= right 里的最小值
        heapq.heappush(self.right, -heapq.heappop(self.left))

        # 保证 left 数量不少于 right
        if len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]

        return (-self.left[0] + self.right[0]) / 2