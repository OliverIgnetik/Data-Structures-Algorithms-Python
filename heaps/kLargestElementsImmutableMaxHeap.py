"""
K Largest Elements In An Immutable Max-Heap
Given a max-heap in array representation, return the k largest elements in the heap without performing explicit removals from the max-heap (the heap is immutable).

Example:
Input:
heap = [17, 7, 16, 2, 3, 15, 14]
k = 2

Output: [17, 16]
Explanation:
[17, 7, 16, 2, 3, 15, 14] encodes:

         17
        /  \
       7    16
      / \  /  \
     2  3 15  14

Constraints:
0 <= k <= len(heap)
"""

"""
Complexity
----
Time : O(KlogK) -> O(KlogK (insert K into the other heap))
Space : O(K)

Approach 
----
Wrapping With A Max-Heap
We process the items in another (mutable) max-heap and items get "unlocked"
below items that we have visited to become candidates for being inspected next.
1. Use another heap 

2. Make note of the heap relations 

- the largest item is at index 0 
- the next largest item is one of it's children:
* 2*i+1 or 2*i+2
- When we take the next largest we do not consider its index any more
- If we kept some pointers that traversed the tree we could track the 
candidates

Example
----
- First we put 17 in the mutable heap 
- Then this makes us consider all of its children 
- Once we put the greater of the children into the mutable heap 
all of it's children are now candidates
etc. 
"""


"""
USEFUL INDIRECT REFERENCE FOR THIS PROBLEM

O(N*logK) Approach with heap

We throw away items smaller then
the kth largest item. So that when we grab the smallest item
left in the heap is the kth largest item.
"""
from queue import PriorityQueue


def heap_approach_kth_largest(arr, k):
    q = PriorityQueue()
    for num in arr:
        q.put(num)
        if q.qsize() > k:
            q.get()

    return q.get()
