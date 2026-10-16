def k_smallest(arr, k):
    n = len(arr)
    if k < 0 or k > n:
        return []
    for i in range(k):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr[:k]

print(k_smallest([7, 10, 4, 3, 20, 15], 3))
