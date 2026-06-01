class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        def can(value):
            summ = 0
            for num in nums:
                summ += ((num +value -1) // value)
            if summ <= threshold:
                return True
            return False
        while left < right:
            mid = (left + right) // 2
            if can(mid):
                right = mid
            else:
                left = mid + 1
        return left

# Time: O(n * log(max(nums))), where n = len(nums)
# Space: O(1)
        
