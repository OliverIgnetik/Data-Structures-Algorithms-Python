"""
Counting Inversions
Given an array A[], we call a pair of indices (i, j) an inversion provided that both i < j and A[i] > A[j] hold.

Count the number of inversions in the provided array.

Example #1:
Input: [3, 1, 2]
Output: 2
Explanation: The pairs (0, 1) and (0, 2) are inversions since they satisfy the provided definition. There are no other inversions in this array.

Example #2:
Input: [1, 2, 3, 4]
Output: 0
Explanation: There are no inversions in this array.

Constraints:  Your solution should run in O(n*log(n)) time.
"""

import math


class Solution:
    def countInversions(self, A):
        """
        Interface
        ----
        :type A: list of int
        :rtype: int

        Approach 
        ----
        Merge Sort Approach
        1. We can solve this problem by making a slight modification to the classical merge sort algorithm in which we 
        recursively divide our original array into two equal or almost equal halves, sort these halves, and finally combine them.

        2. During the combining process (where we would merge 2 sorted halves), if we end up taking an element from the right subarray of our original array,
        then we increment our inversion counter by the number of elements remaining to be merged in our left subarray. 

        3. Why? Because if we take an element from our right subarray, then this element's index is greater than the remaining elements in the left subarray, 
        but its value is less than the remaining elements (assuming we give priority to the left subarray when the two elements are equal). 

        4. Thus, the element in the right subarray can form an inversion with any of the remaining elements in the left subarray. 

        The entire process takes O(n*log(n)) time since the runtime is dominated by the merge sort procedure. 
        Furthermore, we use O(n) space due to the additional arrays created in the merge sort procedure.

        Complexity
        ----
        Time : O(NlogN)
        Space : O(N)
        """
        return self.mergesort(A, 0, len(A) - 1)

    # Helper function performing merge sort
    def mergesort(self, A, left, right):
        inversions = 0

        if right > left:
            mid = left + math.floor((right - left) / 2)

            # Recursively count the number of inversions in the left and right subarrays.
            inversions += self.mergesort(A, left, mid)
            inversions += self.mergesort(A, mid + 1, right)

            # Count the number of inversions between the left and right subarrays.
            inversions += self.merge(A, left, mid, right)

        return inversions

    # Merge function to merge 2 sorted arrays
    # in O(n) time
    def merge(self, A, left, mid, right):

        # Create a new array of required size
        B = [None] * (right - left + 1)

        i = left
        j = mid + 1
        placement = 0

        inversions = 0

        # Keep on placing the elements in the new array
        # And simultaneously increase the inversion count
        while i <= mid and j <= right:
            if A[i] <= A[j]:
                B[placement] = A[i]
                i += 1
            else:
                # NOTE: add to inversions if the right array has a smaller number
                B[placement] = A[j]
                j += 1
                # we need to add the right amount of inversions
                inversions += (mid + 1 - i)

            placement += 1

        # Exactly one of the following two while-loops will run.
        # They place the remaining elements to the new array
        while i <= mid:
            B[placement] = A[i]
            i += 1
            placement += 1
        while j <= right:
            B[placement] = A[j]
            j += 1
            placement += 1

        for k in range(left, right + 1):
            A[k] = B[k - left]

        return inversions


arr = [3, 1, 2]
s = Solution()
print(s.countInversions(arr))
