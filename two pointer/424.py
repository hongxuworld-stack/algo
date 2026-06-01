class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        res = 0 
        for right in range(len(s)):
            c = s[right]
            count[c] = count.get(c,0) + 1
            max_count = max(count.values())
            while right - left + 1 - max_count >k:
                count[s[left]] -= 1
                left +=1
            res = max(res,right - left + 1)
        return res