# Python program for implementation of heap Sort

# To heapify subtree rooted at index i.
# n is size of heap

# COMPLEXITY ANALYSIS
# O(NlogN) time complexity

def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1	 # left = 2*i + 1
    r = 2 * i + 2	 # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[largest] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        # Heapify the root.
        heapify(arr, n, largest)

# The main function to sort an array of given size


def heapSort(arr):
    n = len(arr)

    # Build a maxheap. Notice the reversed order of traversal from
    # the halfway point of the list
    for k in range(n//2 - 1, -1, -1):
        heapify(arr, n, k)

    # Traverse the list in reverse. Heapify the remaining elements each time you place the maximum
    # at the end of list
    for k in range(n-1, 0, -1):
        arr[k], arr[0] = arr[0], arr[k]  # swap
        heapify(arr, k, 0)


# Driver code
arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print("Sorted array is")
print(arr)
# This code is contributed by Mohit Kumra
