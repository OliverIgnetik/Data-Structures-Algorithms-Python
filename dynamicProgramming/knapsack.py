"""
References
- https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/ GeeksforGeeks
- https://www.youtube.com/watch?v=qOUsP4eoYls&list=PLyEvk8ZeQDMVbsg7CEfT0NV3s3GkMx1vN&index=10 CSbreakdown
"""

"""
The 0-1 Knapsack Problem
We are given an array of values values and an array of weights weights:
values[i] corresponds to the value of the i'th item
weights[i] corresponds to the weight of the i'th item

Given these two lists and an integer maxWeight, find a subset of the items in this "knapsack" that has maximal overall value, yet stays <= maxWeight in total weight.

Example 1:
Input:
values = [60, 50, 70, 30]
weights = [5, 3, 4, 2]
maxWeight = 8

Output: 120
Explanation: We take items 1 and 2 (zero-indexed) for a total value of 120 and a total weight of 7.

Example 2:
Input:
values = [60, 100, 120, 80, 30]
weights = [10, 20, 30, 40, 50]
maxWeight = 400

Output: 390
Explanation: We take all items for a total value of 390 and a total weight of 150, still below 400.

Constraints:
You can not split an item
Once you select an item you can not select it again
NOTE: this is a 0/1 problem because we can not subdivide the potential items
"""


class TopDownNoMemoizationSolution:
    def knapsack(self, values, weights, maxWeightConstraint):
        """
        Interface
        ----
        :type values: list of int
        :type weights: list of int
        :type maxWeightConstraint: int
        :rtype: int

        Approach 
        ----
        1. At each stack frame we find the answer to the subproblems
        a) Including this item
        b) Not including this item

        2. Identify the base case

        Complexity
        ---- 
        Related to power sets 
        - We either choose an item or exclude it
        Time : O(2^items)
        Space : O(1)
        """
        return self.knapsack_helper(values, weights, maxWeightConstraint, len(values))

    def knapsack_helper(self, values, weights, max_weight_constraint, total_items):
        """
        If we have no items to use or have to solve the problem with
        a weight upper bound of 0 then the total value that can be
        made is 0. Not items can be choosen.
        """
        # NOTE: BASE CASES
        # zero weight or no items left
        if (total_items == 0 or max_weight_constraint == 0):
            return 0

        """
        Can the current item be used? If it is heavier than the remaining capacity
        to fill, it cannot be considered. We just move on to reducing the subproblem
        to only consider all items behind this item in the knapsack (the array).
        """
        current_item_index = total_items - 1
        if (weights[current_item_index] > max_weight_constraint):
            return self.knapsack_helper(values, weights, max_weight_constraint, total_items - 1)

        """
        The answer to this subproblem we need ask which is the better outcome between:
        1.) Using the current item:
            a.) Add its value
            b.) Determine subproblem answer with target weight reduced & total items considered reduced
            (this item no longer considered)
        2.) Not using the current item
            a.) Don't use the item's value
            b.) Determine subproblem answer with total items considered reduced (this item no longer considered)
        """
        # with_item
        # NOTE: move onto the next item
        with_item = values[current_item_index] + self.knapsack_helper(
            values, weights, max_weight_constraint - weights[current_item_index], total_items - 1)
        # without_item
        # NOTE: we don't subtract it's weight or it's value
        without_item = self.knapsack_helper(
            values, weights, max_weight_constraint, total_items - 1)

        # return the winner of the subproblem competition
        return max(with_item, without_item)


class TopDownSolution:
    def knapsack(self, values, weights, maxWeightConstraint):
        """
        Interface
        ----
        :type values: list of int
        :type weights: list of int
        :type maxWeightConstraint: int
        :rtype: int

        Approach 
        ----
        Build from the top down
        1. Identify subproblems (every cell in the cache represents a subproblem)

        2. Set up a cache to trim the recursion tree

        3. The cache will have dimensions where :
        - the rows represent item sets
        - columns represent the weight constraint

        Complexity
        ----
        Time : O(weights*items)
        Space : O(weights*items)
        """

        # Make a 2D Array of size (values.size()+1)X(maxWeightConstraint+1)
        # And Initalise it with 0
        cache = [[0 for x in range(maxWeightConstraint + 1)]
                 for x in range(len(values) + 1)]

        return self.knapsack_top_down(values, weights, maxWeightConstraint, len(values), cache)

    def knapsack_top_down(self, values, weights, max_weight_constraint, total_items, cache):

        # If total Items are 0 or maxWeightConstraint is 0
        # We can not add any Items
        # NOTE: BASE CASE
        # no weight or no items
        if (total_items == 0 or max_weight_constraint == 0):
            return 0

        # Check for the prestored value and return it
        # This optimises the solution and blocks the recursion for same value
        # NOTE: MEMOIZATION
        if (cache[total_items][max_weight_constraint] != 0):
            return cache[total_items][max_weight_constraint]

        """
        Can the current item be used? If it is heavier than the remaining capacity
        to fill, it cannot be considered. We just move on to reducing the subproblem
        to only consider all items behind this item in the knapsack (the array).
        """
        current_item_index = total_items - 1
        if (weights[current_item_index] > max_weight_constraint):
            cache[total_items][max_weight_constraint] = self.knapsack_top_down(
                values, weights, max_weight_constraint, total_items - 1, cache)

            return cache[total_items][max_weight_constraint]
        """
        The answer to this subproblem we need to ask which is the better outcome between:
            1.) Using the current item:
                a.) Add its value
                b.) Determine subproblem answer with target weight reduced & total items considered reduced
                (this item no longer considered)
            2.) Not using the current item
                a.) Don't use the item's value
                b.) Determine subproblem answer with total items considered reduced (this item no longer considered)
        """
        # with_item
        with_item = values[current_item_index] + self.knapsack_top_down(
            values, weights, max_weight_constraint - weights[current_item_index], total_items - 1, cache)
        # without_item
        without_item = self.knapsack_top_down(
            values, weights, max_weight_constraint, total_items - 1, cache)

        # fill the cache with the winner
        cache[total_items][max_weight_constraint] = max(
            with_item, without_item)

        return cache[total_items][max_weight_constraint]


class BottomUpSolution:
    def knapsack(self, values, weights, maxWeightConstraint):
        """
        Interface
        ----
        :type values: list of int
        :type weights: list of int
        :type maxWeightConstraint: int
        :rtype: int

        Approach
        ----
        Build from the base cases

        Complexity
        ----
        Time : O(weight*items)
        Space : O(weight*items)
        """

        # Create a 2D Array of Size value.size()+1 X maxWeightConstraint+1
        # Initialise it with 0
        cache = [[0 for x in range(maxWeightConstraint + 1)]
                 for x in range(len(values) + 1)]

        # Fill up the cache in Bottom Up Manner
        for total_items in range(0, len(values) + 1):
            for max_weight in range(0, maxWeightConstraint + 1):

                current_item = total_items - 1

                # Case when number of Items are 0 OR maxWeight is 0
                # NOTE: BASE CASES
                if (total_items == 0 or max_weight == 0):
                    cache[total_items][max_weight] = 0

                # If weight of current Item is greater than maxWeight
                # We cannot add that item
                elif (weights[current_item] > max_weight):
                    cache[total_items][max_weight] = cache[total_items - 1][max_weight]

                # Else check the condition of with Item or Without Item
                # And Store the maximum of both
                else:
                    # 1.) With Item -> Go up 1 row & left 'weights[currentItem]' columns and
                    # include the current items value
                    with_item = values[current_item] + \
                        cache[total_items - 1][max_weight -
                                               weights[current_item]]
                    # 2.) Without Item -> Going up 1 row
                    without_item = cache[total_items - 1][max_weight]
                    # cache the winner
                    cache[total_items][max_weight] = max(
                        with_item, without_item)

        return cache[len(values)][maxWeightConstraint]


values = [60, 50, 70, 30]
weights = [5, 3, 4, 2]
maxWeight = 8

s1 = TopDownNoMemoizationSolution()
s2 = TopDownSolution()
s3 = BottomUpSolution()

print(s1.knapsack(values, weights, maxWeight))
print(s2.knapsack(values, weights, maxWeight))
print(s3.knapsack(values, weights, maxWeight))
