from typing import List


class Solution:
    def counting_sort(self, arr: List[int]) -> List[int]:
        c0 = c1 = c2 = 0

        for num in arr:
            if num == 0:
                c0 += 1
            elif num == 1:
                c1 += 1
            else:
                c2 += 1

        arr[:c0] = [0] * c0
        arr[c0:c0 + c1] = [1] * c1
        arr[c0 + c1:] = [2] * c2
        return arr

    def three_pointer_approach(self, arr: List[int]) -> List[int]:
        """
        Complexity 
        Time : O(N) Single pass sorting
        Space : O(1)
        """
        i, l, r = 0, 0, len(arr) - 1
        # everything to the right of r is 2
        # everything in between is 1
        # everything to the left of l is 0

        while i < len(arr):
            if arr[i] == 2 and i < r:
                # move element to end of the array
                arr[i], arr[r] = arr[r], arr[i]
                # r got what it wanted so decrement
                r -= 1
            elif arr[i] == 0 and i > l:
                # move element to the beginning of the array
                arr[i], arr[l] = arr[l], arr[i]
                # l got what it wanted so increment
                l += 1
            else:
                # this is the pivot so don't touch it
                i += 1
        return arr

    def dutch_flag_partition_approach(self, arr: List[int]) -> List[int]:
        """
        This is like the dutch national flag problem 

        input 
        ----
        arr : array of integers from 0 - 2
        output
        ----
        arr : sorted array of integers

        Complexity 
        Time : O(N) single pass sorting
        Space : O(1)
        """
        pivot = 1
        smaller, equal, larger = 0, 0, len(arr)

        while equal < larger:

            # item at equal is less then the pivot
            if arr[equal] < pivot:
                # swap smaller and equal
                arr[smaller], arr[equal] = arr[equal], arr[smaller]
                # smaller got what it wanted and equal got what it wanted
                smaller, equal = smaller + 1, equal + 1
            # item at equal is the pivot
            elif arr[equal] == pivot:
                # equal got what it wanted
                equal += 1
            # item at equal is greater then the pivot
            else:
                # larger got what it wanted
                larger -= 1
                # swap larger and equal
                arr[equal], arr[larger] = arr[larger], arr[equal]

        return arr


print(Solution().three_pointer_approach([0, 1, 2, 1, 2, 2, 2, 1, 0]))
