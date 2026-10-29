class Solution:
    def shipWithinDays(self, weights, days):
        lo = weights[0]
        hi = 0
        for weight in weights:
            if weight > lo:
                lo = weight
            hi += weight

        answer = hi

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            required_days = 1
            current_load = 0

            for weight in weights:
                if current_load + weight <= mid:
                    current_load += weight
                else:
                    required_days += 1
                    current_load = weight

            if required_days <= days:
                answer = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return answer