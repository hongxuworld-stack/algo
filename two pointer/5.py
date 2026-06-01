class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""
        def expnad(left,right):
            while left >=0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        for i in range(len(s)):
            odd = expnad(i,i)
            even = expnad(i,i+1)
            if len(odd) > len(res):
                res = odd
            if len(even) > len(res):
                res = even
        return res  