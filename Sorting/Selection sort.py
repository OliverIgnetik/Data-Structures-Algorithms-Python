def selectionsort(arr):
    i = 0
    while i < len(arr):
        min_value = arr[i]
        index = i
        for j in range(i+1, len(arr)):
            if arr[j] < min_value:
                index = j
                # min_value = arr[j]
        arr[i], arr[index] = arr[index], arr[i]
        i += 1

    return arr


arr = [8, 6, 5, 0, 4, 3, 2]
print(selectionsort(arr))
