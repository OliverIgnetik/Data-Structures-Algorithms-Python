from typing import List


def even_odd_partition(arr: List[int]) -> List[int]:
    """
    Partition an array into even and odd sections
    Complexity 
    Time : O(N) there are no dependent passes over the array
    Space : O(1) we use pointers to save space
    """
    def swap(i, j):
        temp = arr[j]
        arr[j] = arr[i]
        arr[i] = temp

    i = 0
    j = len(arr) - 1
    while i < j:
        if arr[i] % 2 == 0:
            # pointer is satisfied so increment
            i += 1
        else:
            # we need to swap an odd element to the end of the array
            # the odd pointer gets what it wanted so decrement
            swap(i, j)
            j -= 1

        if arr[j] % 2 != 0:
            # pointer gets what it wanted so decrement
            j -= 1
        else:
            # we need to swap the even element to the front of the array
            # the even pointer gets what it wanted so increment
            swap(i, j)
            i += 1

    return arr


arr = [13, 11, 15, 14, 2, 1, 3, 6]

print(even_odd_partition(arr))
