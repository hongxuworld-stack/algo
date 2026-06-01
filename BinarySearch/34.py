class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower_bound(target):
            left = 0
            right = len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            return left
        p1 = lower_bound(target)
        p2 = lower_bound(target+1) -1
        if p1< len(nums) and nums[p1] == target:
            return [p1,p2]
        return [-1,-1]

# Time: O(log n)
# Space: O(1)
