class Solution:
    def findPeakElement(self, nums):
        lo = 0
        hi = len(nums) - 1

        while lo < hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] < nums[mid + 1]:
                # Slope rises; peak exists on the right
                lo = mid + 1
            else:
                # Slope falls; peak is at mid or to the left
                hi = mid

        return lo