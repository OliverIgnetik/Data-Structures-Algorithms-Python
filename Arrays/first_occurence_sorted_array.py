from typing import List


def first_occurence_sorted_array(arr: List[int], val) -> int:
    """
    Returns the first occurence of a value in a sorted array 

    input
    ----
    arr : list of integers (assume non-unique)
    val : value to be searched

    output
    ----
    index : index of first occurance of val in arr

    Complexity
    ----
    Time : O(logN) ie. we half the search space with each decision
    Space : O(1)
    """
    # edge case
    if len(arr) < 2:
        return 0

    left = 0
    right = len(arr) - 1
    index = (left + right) // 2
    while left <= right:
        # edge case
        if index == 0 and arr[index] == val:
            return index
        # general condition for first occurence of val
        if arr[index] == val and arr[index - 1] != val:
            return index
        # look in right half
        if val > arr[index]:
            left = index + 1
        # look in left half
        # this also takes care of the case where we
        # have not yet found the first occurence
        else:
            right = index - 1

        index = (left + right) // 2

    raise ValueError(f'{val} not in array')


arr = [1, 2, 2, 3, 4, 5, 5, 5, 5, 8, 8, 8]

try:
    print(first_occurence_sorted_array(arr, 0))
except ValueError as err:
    print(err)
