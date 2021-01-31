def insertionsort(arr):
    length = len(arr)
    i = 1
    end = arr[0]
    while i < length:
        if arr[i] < end:
            x = arr.pop(i)
            for j in range(0, i):
                if x < arr[j]:
                    arr.insert(j, x)
                    break
        end = arr[i]
        i += 1
    return arr


def insertion_sort(arr):

    # For every index in array
    for i in range(1, len(arr)):

        # Set current values and position
        currentvalue = arr[i]
        position = i

        # this is a good solution if you don't care about writing costs
        # Sorted Sublist
        while position > 0 and arr[position-1] > currentvalue:
            # shift items to the right if they are bigger
            arr[position] = arr[position-1]
            position -= 1

        arr[position] = currentvalue
    return arr


arr = [6, 5, 3, 1, 8, 7, 2, 4]
# print(insertion_sort(arr))
print(insertionsort(arr))
