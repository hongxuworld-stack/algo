# Given a sorted non-decreasing list of integers, find the first index where each distinct number appears.
# For example:
# Input:
# nums = [1,1,1,2,2,2,2,3,3,3,3,4,4,4,5,5,5]
# Output:
# {
#     1: 0,
#     2: 3,
#     3: 7,
#     4: 11,
#     5: 14
# }
class Solution: 
    def findFirstPositions(self, nums: List[int]) -> Dict[int, int]:
        res = {}
        def helper(left, right):
            if left > right:
                return
            if nums[left] == nums[right]:
                num = nums[left]
                # if num not in res:
                #     res[num] = left
                if num not in res:
                    res[num] = left
                else:
                    res[num] = min(res[num], left)
                return
            mid = (left + right) // 2
            helper(left,mid)
            helper(mid +1,right)
        helper(0, len(nums) - 1)
        return res