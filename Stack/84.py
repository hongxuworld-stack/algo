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
    

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        stack = []
        max_res = 0
        for i, height in enumerate(heights):
            while len(stack) > 0 and height < heights[stack[-1]]:
                pop_location = stack.pop()
                h = heights[pop_location]
                area = h * (i - stack[-1] -1)
                max_res = max(max_res, area)
            stack.append(i)
        return max_res
    # stack[-1] 表示左边一个更矮的