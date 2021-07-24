"""
Generate The Powerset
Given an input sequence arr, generate its power set.

A "power set" is the set of all subsets that can be formed from a sequence/set.

A set is a collection of distinct objects. A subset is a set that only contains elements found in the original set.

Example:
Input: [1, 2, 3]
Output:
[
  [], # the empty set
  [1,2,3], NOTE: if we only allowed strict subsets we could not include this
  [1,2],
  [1,3],
  [1],
  [2,3],
  [2],
  [3]
]

Constraints:
All items in the provided sequence will be unique
"""

from copy import deepcopy


class Solution:
    def powerset(self, inputSet):
        """
        Interface
        ----
        :type inputSet: list of int
        :rtype: list of list of int

        Approach
        ----

        1. Draw the recursion tree

        2. Establish a policy and the associated logic to enforce at each stack frame

        3. Establish constraints and backtracking conditions 

        Complexity
        ----
        Recurrence relation 
        T(N) = 2T(N-1) + O(1)

        O(1) -> binary decision at each stackframe
        NOTE: we will always have a perfect tree with our recursion
        branching factor = 2 
        depth = N 

        Generic for these types of recurrence relations
        Time : O(2^N)
        Space : O(N) not including the output
        """
        powerset = []
        self.generate_powerset(0, [], inputSet, powerset)

        return powerset

    def generate_powerset(self, current_index, selected_so_far, input_set, powerset):
        """
        Base case: when we have made n decisions then we have
        expressed a 'path'. We reap that path here and return
        to continue the recursion.
        """
        if current_index == len(input_set):
            # we need a deepcopy so we don't just copy references
            powerset.append(deepcopy(selected_so_far))
            return

        """
        Recurse WITH the item at 'currentIndex' in the powerset we
        are working on.
        """
        selected_so_far.append(input_set[current_index])
        self.generate_powerset(
            current_index + 1, selected_so_far, input_set, powerset)

        # When the recursion returns, remove the choice we made
        # ie. backtrack
        selected_so_far.pop()

        """
        Recurse WITHOUT the item at 'currentIndex' in the powerset
        we are working on.
        """
        self.generate_powerset(
            current_index + 1, selected_so_far, input_set, powerset)


i = [1, 2, 3]
s = Solution()
print(s.powerset(i))
