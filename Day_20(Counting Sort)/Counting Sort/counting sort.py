def counting_sort(arr):
    if len(arr) == 0:
        return []
    largest = max_value(arr)
    count = [0] * (largest + 1)
    for num in arr:
        count[num] += 1
    result = []
    for num in range(len(count)):
        for _ in range(count[num]):
            result.append(num)
    return result

def max_value(arr):
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num

    return largest

print(counting_sort([4, 2, 2, 1, 3, 4, 1]))
