"""
Permutations
Given an array arr, return all the permutations of the array.

Example 1:
Input: [1,2]
Output:
[
  [1,2],
  [2,1]
]

Example 2:
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

Constraints:
arr will have all unique values
The order you return the permutations does not matter
"""
from copy import deepcopy


class Solution:
    def permute(self, originalArray):
        """
        Interface
        ----
        :type originalArray: list of int
        :rtype: list of list of int

        Approach 
        ----

        1. Establish the decision space at each stack frame

        2. Understand how the state changes the decision space 

        3. Identify base cases and constraints

        Complexity
        ----
        Time : O(N!)
        The exact amount T(N) is O(eN!) 
        NOTE: the branching factor is changing by 1 at each placement slot

        Space : O(N) call stack depth
        """
        permutations = []
        self.generate_all_permutations([], originalArray, permutations)

        return permutations

    def generate_all_permutations(self, running_choices, original_array, permutations):

        # Base Case
        if len(running_choices) == len(original_array):
            permutations.append(deepcopy(running_choices))
            return

        # Every stack frame of this function call represents the expression of trying (almost) all items in every "slot" in the array.
        # The recursion stops when we are choosing on 1 past the final "slot".
        for i in range(0, len(original_array)):
            choice = original_array[i]

            # Skip if element already exists in 'runningChoices'
            if choice in running_choices:
                continue

            # 1.) Choose - Add the item to the 'runningChoices'
            running_choices.append(choice)

            # 2.) Explore - Recurse on the choice
            self.generate_all_permutations(
                running_choices, original_array, permutations)

            # 3.) Unchoose/BACKTRACK - We have returned from the recursion, remove the choice we made.
            # The next iteration will try another item in the "slot" we are working on.
            running_choices.pop()


i = [1, 2, 3]
s = Solution()
print(s.permute(i))
