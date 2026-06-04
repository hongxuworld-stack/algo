class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t_len = len(temperatures)
        stack = []
        res = [0 for _ in range(t_len)]
        for i,temp in enumerate(temperatures):
            while len(stack) >0 and temp > temperatures[stack[-1]]:
                pop_location = stack.pop()
                res[pop_location] = i - pop_location
            stack.append(i)
        return res

