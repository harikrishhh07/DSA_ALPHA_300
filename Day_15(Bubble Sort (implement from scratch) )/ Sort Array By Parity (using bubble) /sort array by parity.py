def sort_by_parity(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] % 2 != 0 and arr[j + 1] % 2 == 0:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

print(sort_by_parity([3, 1, 2, 4]))
