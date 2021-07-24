"""
Minimum Weight Path In A Triangle
Given a 2D array that resembles the shape of a triangle, return the min-cost path from the top to the bottom.

From each cell, you may only go diagonally down to the left or right.

Example:
Input:
[
  [5],
  [1,6],
  [4,3,10],
  [3,2,4,1]
]

Output: 11
Explanation:
2 -> 3 -> 1 -> 5
[
      [5],
    [1,  6],
   [4, 3, 10],
  [3, 2, 4, 1]
]
"""


class Solution:
    def minimumPathCost(self, triangle):
        """
        Interface
        ----
        :type triangle: list of list of int
        :rtype: int

        Approach 
        ----
        1. Break up the problem into subproblems
        2. Use caching to reduce complexity
        3. In this case we start from the bottom and ask:
        - what is the best way to get to the layer that is one step higher
        given we know the best way to get to every node in the current layer?

        NOTE: From each cell, you may only go diagonally down to the left or right.
        ie. we can only go up diagonally right or left when caching and sub-probleming from
        the bottom up

        Complexity
        ----
        Where M = rows, N = cols
        Items = I
        Time : O(I)
        Space : O(N)
        """

        # Store the total layers of the triangle
        total_layers = len(triangle)

        cache = [0] * total_layers
        # Initialize the dpLayerCache with the elements of last layer
        self.initialize_cache_with_last_layer(cache, triangle[-1])

        # Start from the 2nd to last layer
        for row in range(total_layers - 2, -1, -1):
            current_layer = triangle[row]

            # Traverse the current layer
            for col in range(0, len(current_layer)):
                cell_value = current_layer[col]
                # For each node of the ith row
                # The minimum path sum would be
                # The minimum path sum of its 2 children + value of that node
                min_sum_going_left = cache[col]
                min_sum_going_right = cache[col + 1]
                min_sum_direction = min(
                    min_sum_going_left, min_sum_going_right)

                cache[col] = min_sum_direction + cell_value

        # Return the top element
        return cache[0]

    # Helper Function to
    # Initialize the dpLayerCache with the elements of last layer
    def initialize_cache_with_last_layer(self, cache, last_row):
        for i in range(0, len(cache)):
            cache[i] = last_row[i]


triangle = [
    [5],
    [1, 6],
    [4, 3, 10],
    [3, 2, 4, 1]
]

s = Solution()
min_cost = s.minimumPathCost(triangle)
print(min_cost)
