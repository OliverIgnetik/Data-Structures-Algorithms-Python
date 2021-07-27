"""
Given a sequence of integers in an array, find the "next permutation" of the sequence.
If the current permutation is the final permutation in the permutation sequence, return
an array sorted in ascending order.

Example permutation sequence 

1,2,3
1,3,2
2,1,3
2,3,1
3,1,2
3,2,1

Construction of sequence: 
_,_,_ (can use: 1,2,3)
1,_,_ (can use: 2,3)
1,2,_ (can use: 3)
1,2,3 Permutation #1 (choices exhausted - backtrack)
1,2,_ (can use: 3) (already placed 3 - backtrack)
1,_,_ (can use: 3, 2)
1,3,_ (can use: 2)
1,3,2 Permutation #2 (choices exhausted - backtrack)
1,3,_ (can use: 2) (already placed 2 - backtrack)
1,_,_ (can use: 2, 3) (already placed 3 - backtrack)
_,_,_ (can use: 2, 3, 1)
2,_,_ (can use: 3, 1)
2,1,_ (can use: 3)
2,1,3 Permutation #3 (choices exhausted - backtrack)
... and so on


Example 1 
Input: [1,2,3]
Output: [1,3,2]

Example 2 
Input: [1,5,2]
Output: [2,1,5]

Example 3
Input: [3,2,1]
Output: [1,2,3] # Cycle back around to the first permutation

Key to O(N) solution
----
If we know how permutations are constructed we can do this in better then 
factorial time. 
- Backtracking is a large part of this problem
- Case analysis is crucial to adhering to linear time.

We need to think of: 
- Placements and exploring possibilities
- Keeping track of state and the decision space
- Realizing that a strictly decreasing section is on it's last permutation
- We have to module the placement that comes before the strictly decreasing section

Example 
[6,2,1,5,4,3,0]
     *
State and decision space at this point 
[0, 3, 4, 5]

- We can ignore 0 as this current permutation is on 1 and thus we have passed choosing 0.
- Since 6 and 2 are already placed we have to pick 3 as the replacement for 1.
- We pick the next greatest item from 1 (which is 3)
- We then change the sequence to a strictly increasing section starting from 3.
"""

from typing import List, Tuple


class Solution1:

    def find_strictly_decreasing_sequence(self, arr: List[int]) -> int:
        i = len(arr) - 2
        while arr[i] > arr[i + 1]:
            i -= 1
        return i

    def reverse_sequence(self, arr: List[int], start: int) -> None:
        i, j = start, len(arr) - 1
        while i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    def find_next_greatest_item(self, arr: List[int], current_placement: int, start: int) -> int:
        # what about the case where the current placement is the largest element in the array?
        # The only time this can occur is if the strictly decreasing sequence starts from index 0
        index_to_swap = start
        min_item = arr[start]
        for i in range(start, len(arr)):
            if arr[i] < min_item and arr[i] > current_placement:
                index_to_swap = i
                min_item = arr[i]
        return index_to_swap

    def next_permutation(self, arr: List[int]) -> List[int]:
        """
        We only need to perform linear passes to perform the necessary sub routines

        We assume that the list of integers is unique
        Complexity
        ----
        Time : O(N)
        Space : O(1)
        """
        # find the current placement index by finding the element index that is just before
        # a strictly decreasing sequence
        placement_to_swap_index = self.find_strictly_decreasing_sequence(
            arr)

        # ie. if we have placed the last placement (ie. biggest number) in the first slot we can
        # just reverse the array
        if placement_to_swap_index == -1:
            self.reverse_sequence(arr, 0)
            return arr

        # grab the value of the current placement
        current_placement = arr[placement_to_swap_index]
        # the sub array starts from the next index
        start_index_decreasing_sub_array = placement_to_swap_index + 1
        # use the current placement and the start of the decreasing sequence to find the next greatest item
        # in the decreasing sequence
        next_greatest_item_index = self.find_next_greatest_item(
            arr, current_placement, start_index_decreasing_sub_array)
        # swap the two
        arr[placement_to_swap_index], arr[next_greatest_item_index] = arr[next_greatest_item_index], arr[placement_to_swap_index]
        # then reverse the sequence
        self.reverse_sequence(arr, start_index_decreasing_sub_array)
        return arr


s = Solution1()
# example from video
arr1 = [6, 2, 1, 5, 4, 3, 0]
arr2 = [3, 4, 9, 5, 4, 3, 2]
arr3 = [3, 2, 1]
arr4 = [1, 2, 3]

print(s.next_permutation(arr1))
print(s.next_permutation(arr2))
print(s.next_permutation(arr3))
print(s.next_permutation(arr4))
