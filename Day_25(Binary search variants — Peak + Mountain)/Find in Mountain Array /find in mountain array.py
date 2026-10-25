class Solution:
    def findInMountainArray(self, target, mountain_arr):
        n = mountain_arr.length()
        lo = 0
        hi = n - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2

            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                lo = mid + 1
            else:
                hi = mid

        peak = lo
        lo = 0
        hi = peak

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            value = mountain_arr.get(mid)

            if value == target:
                return mid
            elif value < target:
                lo = mid + 1
            else:
                hi = mid - 1

        lo = peak + 1
        hi = n - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            value = mountain_arr.get(mid)

            if value == target:
                return mid
            elif value < target:
                hi = mid - 1
            else:
                lo = mid + 1

        return -1
