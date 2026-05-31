class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed = max(piles)
        left = 1
        right = max(piles)
        while left < right:
            total_hour = 0
            mid = (left + right) // 2
            for pile in piles:
                total_hour += ((pile + mid -1) // mid)
            if total_hour <= h:
                min_speed = mid
                right = mid
            else:
                left = mid + 1 
        return min_speed