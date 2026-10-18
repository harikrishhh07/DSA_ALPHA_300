
def merge_count(left, right):
    result = []
    i = 0
    j = 0
    count = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            count += len(left) - i
            j += 1

    result += left[i:]
    result += right[j:]

    return result, count

def count_inversions(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2

    left, a = count_inversions(arr[:mid])
    right, b = count_inversions(arr[mid:])

    merged, c = merge_count(left, right)

    return merged, a + b + c

arr = [2, 4, 1, 3, 5]
sorted_arr, count = count_inversions(arr)

print("Sorted array:", sorted_arr)
print("Inversions:", count)
