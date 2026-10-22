class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo = 1
        hi = n
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if isBadVersion(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo
