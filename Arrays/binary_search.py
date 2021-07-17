from typing import List


def binary_search(arr: List[int], val: int) -> int:
    """
    Returns the index of a value in an array of unique integers

    input 
    ----
    arr : sorted array of integers (assume that the integers are unique)
    val : value for search (int)

    output
    ---- 
    index : index of val in arr

    Complexity 
    Time : O(logN)
    Space : O(1)
    """

    left = 0
    right = len(arr) - 1
    index = (left + right) // 2
    while left <= right:
        if arr[index] == val:
            return index
        if val > arr[index]:
            left = index + 1
        else:
            right = index - 1

        index = (left + right) // 2

    raise ValueError(f'{val} not found in array')


print(binary_search([1, 2, 4, 5, 6, 10, 12, 15, 20], 3))
