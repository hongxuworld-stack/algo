class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        n = len(heights)
        stack = []
        left = [0 for _ in range(n)]
        right = [0 for _ in range(n)]
        for i,height in enumerate(heights):
            while len(stack) and heights[stack[-1]] > height:
                pop_location = stack.pop()
                right[pop_location] = i - pop_location
            stack.append(i)
        stack = []
        for i in range(n-1,-1,-1):
            height = heights[i]
            while len(stack) and heights[stack[-1]] > height:
                pop_location = stack.pop()
                left[pop_location] = pop_location - i
            stack.append(i)
        res = 0
        for i in range(n):
            width = left[i] + right[i] - 1
            res = max(res, heights[i] * width)
        return res 