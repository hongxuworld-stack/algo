class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        area = 0
        heights = [0 for _ in range(cols)]
        # for row in range(rows):
        #     heights = [0 for _ in range(cols)]
        #     for col in range(cols):
        #         cur_row = row
        #         height = 0
        #         while cur_row>=0 and matrix[cur_row][col] == "1":
        #             height +=1
        #             cur_row -= 1
        #         heights[col] = height
        #     print(heights)
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "1":
                    heights[c] += 1
                else:
                    heights[c] = 0
            area = max(area,self.largestRectangleArea(heights))
        return area
            
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