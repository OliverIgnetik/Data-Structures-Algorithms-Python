from queue import PriorityQueue
"""
MASTER THEOREM for Recurrence Relations
T(n) = aT(n/b) + cn^k 

T(n) is O(n^k) if a < b^k
T(n) is O(n^klog_b(n)) if a = b^k
T(n) is O(n^(log_b(a))) if a < b^k
"""

"""
Sorting method will most likely be quick sort or merge sort 
O(NlogN)
Access is constant time
"""


def simple_method(arr, k):
    arr.sort()
    return arr[len(arr) - k]


"""
O(N*logK) Approach with heap

We throw away items smaller then
the kth largest item. So that when we grab the smallest item
left in the heap is the kth largest item.
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

Recurrence relation 

T(n) = T(n/2) + O(n)

Using the master theorem 
a = 1, b = 2, c = 1, k = 1
b^k = 2 > a

T(n) is O(n)

We can do a partition and eliminate half of the search space (on average).
It works given the fact that in a sorted array:
- The kth largest item must be at index (n-k)
- Generally speaking we know if we do a partition then
kth largest item should be at an index greater then the index of pivot.
Then we should focus our search on the items with greater indices.
"""


import math
import random


def quickselect(arr, k):
    '''
    :type arr: list of int
    :type k: int
    :rtype: int
    '''

    # helper functions
    def partition(arr, left, right, pivot_index):
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

    def swap(arr, first, second):
        temp = arr[first]
        arr[first] = arr[second]
        arr[second] = temp

    n = len(arr)
    left = 0
    right = n - 1

    while left <= right:
        # Random pivot index will ensure on average we avoid
        # O(N^2) runtime
        pivot_index = random.randint(left, right)

        chosen_pivot_index = partition(
            arr, left, right, pivot_index)

        # What does the 'finalIndexOfChoosenPivot' tell us?
        if (chosen_pivot_index == n - k):

            # If the pivot index is the (n-k)th index then we are done and can stop here
            return arr[chosen_pivot_index]
        elif (chosen_pivot_index > n - k):
            # k'th largest must be in the left partition.
            right = chosen_pivot_index - 1
        else:
            # finalIndexOfChoosenPivot < n - k
            # k'th largest must be in the right partition.

            left = chosen_pivot_index + 1

    return -1


arr = [8, 1, 3, 2, 6, 7]

print(heap_approach(arr, 2))
print(quickselect(arr, 2))
