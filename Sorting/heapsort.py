# Python program for implementation of heap Sort

# To heapify subtree rooted at index i.
# n is size of heap

# COMPLEXITY ANALYSIS
# O(NlogN) time complexity

from heapq import heappush, heappop

#################### PYTHON DOCS IMPLEMENTATION ##################################
# https://docs.python.org/2/library/heapq.html#priority-queue-implementation-notes
# this works more succintly because we make use of a minheap not a maxheap


def heapsort_alt(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for _ in range(len(h))]


#################### MAXHEAP GEEKSFORGEEKS IMPLEMENTATION ##################################
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1
    r = 2 * i + 2

    # check if left child is greater
    if l < n and arr[largest] < arr[l]:
        largest = l

    # check if right child is greater
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Heapify the root.
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    # Build a maxheap. Notice the reversed order of traversal from
    # the halfway point of the list
    for k in range(n//2 - 1, -1, -1):
        heapify(arr, n, k)

    # Heapify the remaining elements, each time you place the maximum
    # at the end of list
    for k in range(n-1, 0, -1):
        arr[k], arr[0] = arr[0], arr[k]  # swap
        heapify(arr, k, 0)


############################### TEST ####################################
arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print("Sorted array is")
print(arr)

print(heapsort_alt(arr))
