class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        stack = []
        max_res = 0
        for i, height in enumerate(heights):
            while len(stack) > 0 and height < heights[stack[-1]]:
                pop_location = stack.pop()
                left_height = heights[pop_location]
                area = left_height * (i - stack[-1] -1)
                max_res = max(max_res, area)
            stack.append(i)
        return max_res