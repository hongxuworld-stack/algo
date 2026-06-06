import heapq
class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        left_max = float("inf")
        # right_min = float("inf")
        if len(self.left):
            left_max = - self.left[0]
        if num < left_max:
            heapq.heappush(self.left, - num)
        else:
            heapq.heappush(self.right, num)
        if len(self.left) > len(self.right) + 1:
            left_max = - heapq.heappop(self.left)
            heapq.heappush(self.right,left_max)
        elif len(self.right) > len(self.left) + 1:
            right_min = heapq.heappop(self.right)
            heapq.heappush(self.left, - right_min)
        
    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2
        elif len(self.left) > len(self.right):
            return -self.left[0]
        else:
            return self.right[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()