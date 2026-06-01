from collections import defaultdict
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        res = [0] * n
        n2_position_map = defaultdict(set)
        for i,num in enumerate(nums2):
            n2_position_map[num].add(i)
        nums2.sort(reverse=True)
        nums1.sort(reverse=True)
        left = 0
        right = len(nums1) -1 
        for num in nums2:
            or_i = n2_position_map[num].pop()
            if nums1[left] > num:
                res[or_i] = nums1[left]
                left += 1
            else:
                res[or_i] = nums1[right]
                right -= 1
        return res
