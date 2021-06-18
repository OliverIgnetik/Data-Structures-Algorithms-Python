from queue import PriorityQueue

# O(NlogN)


def simple_method(arr, k):
    arr.sort()
    return arr[len(arr) - k]


"""
O(N*logK) Approach with heap

We throw away items that items smaller then
the kth largest item. So that we grab the smallest item
left in the heap is the second largest item.
"""


def heap_approach(arr, k):
    q = PriorityQueue()
    for num in arr:
        q.put(num)
        if q.qsize() > k:
            q.get()

    return q.get()


"""
O(N) Approach using partitions 
Think of BUD (Bottlenecks, Unnecessary work, Duplicate work)

We can do a partition and eliminate half of the search space (on average)self.
It works on the fact that in a sorted array:

- The kth largest item must be at index n-k
- Generally speaking if we do a partition then if we know the
kth largest item should be at an index greater then the index of pivot
then we should focus our search on the items with greater indices (or to the right)
"""


import math
import random


def kthLargest(arr, k):
    '''
    :type arr: list of int
    :type k: int
    :rtype: int
    '''
    n = len(arr)
    left = 0
    right = n - 1

    while left <= right:
        # Random pivot index will ensure on average we avoid
        # O(N^2) runtime
        choosen_pivot_index = random.randint(left, right)

        final_index_of_choosen_pivot = partition(
            arr, left, right, choosen_pivot_index)

        # What does the 'finalIndexOfChoosenPivot' tell us?
        if (final_index_of_choosen_pivot == n - k):

            # If the pivot index in the (n-k)th index then we are done and can stop here
            return arr[final_index_of_choosen_pivot]
        elif (final_index_of_choosen_pivot > n - k):
            # k'th largest must be in the left partition.
            right = final_index_of_choosen_pivot - 1
        else:
            # finalIndexOfChoosenPivot < n - k

            # k'th largest must be in the right partition.

            left = final_index_of_choosen_pivot + 1

    return -1


def partition(self, arr, left, right, pivot_index):
    pivot_value = arr[pivot_index]
    lesser_items_tail_index = left

    # Move the item at the 'pivotIndex' OUT OF THE WAY. We are about to bulldoze
    # through the partitioning space and we don't want it in the way
    swap(arr, pivot_index, right)

    for i in range(left, right):
        if arr[i] < pivot_value:
            swap(arr, i, lesser_items_tail_index)
            lesser_items_tail_index += 1

    # Ok...partitioning is done. Swap the pivot item BACK into the space we just
    # partitioned at the 'lesserItemsTailIndex'...that's where the pivot item
    # belongs

    # In the middle of the "sandwich".

    swap(arr, right, lesser_items_tail_index)

    return lesser_items_tail_index


def swap(self, arr, first, second):
    temp = arr[first]
    arr[first] = arr[second]
    arr[second] = temp


arr = [8, 1, 3, 2, 6, 7]

print(heap_approach(arr, 2))
