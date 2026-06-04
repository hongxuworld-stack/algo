class Solution:
    def isValid(self, s: str) -> bool:
        pair = {
            '}':'{',
            ')':'(',
            ']':'['
        }
        stack = []
        for item in s:
            if item in "({[":
                stack.append(item)
            else:
                if not stack:
                    return False
                if stack.pop() != pair[item]:
                    return False
        return True if len(stack)==0 else False
        