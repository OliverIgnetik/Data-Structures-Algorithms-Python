"""
Find the k'th Largest or Smallest Element
Given an array arr find the k'th largest element.

Example 1:
Input:
arr = [1,2,3,4,5,6]
k = 1

Output: 6
Explanation: 6 is the 1st largest element

Example 2:
Input:
arr = [1,2,3,4,5,6]
k = 6

Output: 1
Explanation: 1 is the 6th largest element

Constraints:
0 <= k <= len(arr)
"""

import math
import random


class Solution:
    def kthLargest(self, arr, k):
        """
        Interface
        ----
        :type arr: list of int
        :type k: int
        :rtype: int

        Complexity
        ----
        Recurrence Relation 
        O(N) is the partition function that happens at each recursive call

        T(N) = T(N/2) + O(N)
        T(N) is O(N) by the master theorem

        MASTER THEOREM for Recurrence Relations
        T(n) = aT(n/b) + cn^k 

        T(n) is O(n^k) if a < b^k
        T(n) is O(n^klog_b(n)) if a = b^k
        T(n) is O(n^(log_b(a))) if a < b^k

        Time : O(logN)
        Space : O(1)
        """
        n = len(arr)
        left = 0
        right = n - 1

        while left <= right:
            choosen_pivot_index = random.randint(left, right)

            final_index_of_choosen_pivot = self.partition(
                arr, left, right, choosen_pivot_index)

            # What does the 'finalIndexOfChoosenPivot' tell us?
            if (final_index_of_choosen_pivot == n - k):

                # Found. The pivot is index on index n - k. This is literally its final
                # position if the array we were given had been sorted. See how we saved work?
                # We don't need to sort the whole array
                return arr[final_index_of_choosen_pivot]
            elif (final_index_of_choosen_pivot > n - k):
                # k'th largest must be in the left partition. We "overshot" and need to go left
                # (and we do this by narrowing the right bound)
                right = final_index_of_choosen_pivot - 1
            else:
                # finalIndexOfChoosenPivot < n - k

                # k'th largest must be in the right partition. We "undershot" and need to go
                # right (and we do this by narrowing the left bound)

                left = final_index_of_choosen_pivot + 1

        return -1

    def partition(self, arr, left, right, pivot_index):
        pivot_value = arr[pivot_index]
        lesser_items_tail_index = left

        # Move the item at the 'pivotIndex' OUT OF THE WAY. We are about to bulldoze
        # through the partitioning space and we don't want it in the way
        self.swap(arr, pivot_index, right)

        for i in range(left, right):
            if arr[i] < pivot_value:
                self.swap(arr, i, lesser_items_tail_index)
                lesser_items_tail_index += 1

        # Ok...partitioning is done. Swap the pivot item BACK into the space we just
        # partitioned at the 'lesserItemsTailIndex'...that's where the pivot item
        # belongs

        # In the middle of the "sandwich".

        self.swap(arr, right, lesser_items_tail_index)

        return lesser_items_tail_index

    def swap(self, arr, first, second):
        temp = arr[first]
        arr[first] = arr[second]
        arr[second] = temp


from queue import PriorityQueue


class HeapSolution:
    def heap_approach_kth_largest(self, arr, k):
        q = PriorityQueue()
        for num in arr:
            q.put(num)
            if q.qsize() > k:
                q.get()

        return q.get()

    def heap_approach_kth_smallest(self, arr, k):
        q = PriorityQueue()
        for num in arr:
            q.put(-num)
            if q.qsize() > k:
                q.get()

        return -q.get()


arr = [1, 2, 3, 4, 5, 6]
# NOTE: THE ARRAY DOES NOT HAVE TO BE SORTED
k = 2
s = Solution()
print(s.kthLargest(arr, k))
