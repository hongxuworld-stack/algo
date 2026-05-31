class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1
        left = 1
        right = max(bloomDay)
        def can(days):
            bloomed = [1 if bloom <= days else 0 for bloom in bloomDay]
            cur_bloomed_count = 0
            bouquets_count = 0
            for bloom in bloomed:
                if bloom ==1:
                    cur_bloomed_count += 1
                    if cur_bloomed_count == k:
                        cur_bloomed_count = 0
                        bouquets_count +=1
                else:
                    cur_bloomed_count = 0
            return True if bouquets_count>m else False

        while left < right:
            mid = (left + right) // 2
            if can(mid):
                right = mid
            else:
                left = mid + 1
        return left
         