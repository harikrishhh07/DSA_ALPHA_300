class Solution:
    def findPages(self, arr, k):
        n = len(arr)

        if k > n:
            return -1
        lo = arr[0]
        hi = 0
        for pages in arr:
            if pages > lo:
                lo = pages
            hi += pages

        answer = hi

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            students = 1
            current_pages = 0

            for pages in arr:
                if current_pages + pages <= mid:
                    current_pages += pages
                else:
                    students += 1
                    current_pages = pages

            if students <= k:
                answer = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return answer