class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        cur = 0
        stack = []
        for ch in s:
            if ch == "(":
                stack.append(cur)
                cur = 0
            else:
                previous  = stack.pop()
                cur = previous + max(2 * cur, 1)
        return cur

    def scoreOfParentheses2(self, s: str) -> int:
        stack = []
        res = 0
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(ch)
            else:
                stack.pop()
                if s[i-1] == "(":
                    res += 2 ** len(stack)
        return res