def sort_zeros_ones(arr):
    zeros = 0
    for num in arr:
        if num == 0:
            zeros += 1
    for i in range(len(arr)):
        if i < zeros:
            arr[i] = 0
        else:
            arr[i] = 1
    return arr

print(sort_zeros_ones([1, 0, 1, 1, 0, 0, 1]))

