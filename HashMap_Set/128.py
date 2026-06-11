class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0
        for num in nums_set:
            cur = num
            if (cur - 1) not in nums_set:
                l = 1
                while (cur + 1) in nums_set:
                    l += 1
                    cur +=1
                res = max(res,l)
        return res