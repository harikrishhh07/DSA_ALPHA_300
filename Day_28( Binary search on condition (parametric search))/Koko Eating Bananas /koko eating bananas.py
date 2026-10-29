class Solution:
    def minEatingSpeed(self, piles, h):
        lo = 1
        hi = piles[0]

        for pile in piles:
            if pile > hi:
                hi = pile

        answer = hi

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            total_hours = 0

            for pile in piles:
                total_hours += (pile + mid - 1) // mid

            if total_hours <= h:
                answer = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return answer