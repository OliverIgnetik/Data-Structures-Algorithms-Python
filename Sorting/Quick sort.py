# SOLUTION 1
# def quicksort(array, left, right):
#     if left < right:
#         pivot = right
#         partitionindex = partition(array, pivot, left, right)

#         quicksort(array, left, partitionindex - 1)
#         quicksort(array, partitionindex + 1, right)
#     return array


# def partition(array, pivot, left, right):
#     pivotvalue = array[pivot]
#     partitionindex = left  # keeps track of the last swap

#     for i in range(left, right):
#         if array[i] < pivotvalue:
#             swap(array, i, partitionindex)
#             partitionindex += 1
#     # final swap to complete partition
#     swap(array, right, partitionindex)
#     return partitionindex


# def swap(array, firstindex, secondindex):
#     array[firstindex], array[secondindex] = array[secondindex], array[firstindex]
##     temp = array[firstindex]
##     array[firstindex] = array[secondindex]
##     array[secondindex] = temp


# SOLUTION 2


def quick_sort_alt(arr):

    return quick_sort_help(arr, 0, len(arr)-1)


def quick_sort_help(arr, first, last):

    if first < last:

        # find the split point
        splitpoint = partition_alt(arr, first, last)
        # split the list
        quick_sort_help(arr, first, splitpoint-1)
        quick_sort_help(arr, splitpoint+1, last)
    return arr


def partition_alt(arr, first, last):

    pivotvalue = arr[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:
        # increment leftmark
        while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
            leftmark += 1
        # increment rightmark
        while arr[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1
        # stop once we find the split point
        if rightmark < leftmark:
            done = True
        # swap left and right mark
        else:
            swap_alt(arr, leftmark, rightmark)

    # do the final swap
    swap_alt(arr, first, rightmark)
    return rightmark


def swap_alt(array, firstindex, secondindex):
    array[firstindex], array[secondindex] = array[secondindex], array[firstindex]


numbers = [8, 9, 4, 3, 5, 1]

# Select first and last index as 2nd and 3rd parameters
print(quick_sort_alt(numbers))
# partition_test = [1, 3, 10, 8, 5, 4, 7, 6]
# partition(partition_test, len(partition_test) - 1, 0, len(partition_test)-1)
# print(quicksort(numbers, 0, len(numbers)-1))
