class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count=0
        left=0
        product=1
        if k<=1:
            return 0
        for i in range(len(nums)):
            product*=nums[i]
            while product>=k:
                product//=nums[left]
                left+=1
            count+=i-left+1
        return count