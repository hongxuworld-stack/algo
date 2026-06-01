class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        def can(capacity):
            need_days = 1
            cur_weight = 0
            for w in weights:
                if cur_weight + w > capacity:
                    cur_weight = 0
                    need_days +=1
                cur_weight += w
            return need_days <= days

        while left < right:
            mid = (left + right) // 2
            if can(mid):
                right = mid
            else:
                left = mid + 1
        return left

# Time: O(n * log(sum(weights) - max(weights))), where n = len(weights)
# Space: O(1)
