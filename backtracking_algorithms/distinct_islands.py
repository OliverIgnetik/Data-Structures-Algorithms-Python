"""
Number of Distinct Islands
A two-dimensional region is divided by a grid into uniform square cells, each of which represents either “land” or “water”.
The integer 1 is used to represent a square of land.
The integer 0 is used to represent a square of water.

We define an "island" to be a maximal group of type 1 squares ("land") that are adjacent in one of four directions (horizontally or vertically).

Furthermore, we call two islands "distinct" provided that they are unique under translations. That is, one island cannot be shifted horizontally or vertically to obtain the other.

Count the number of distinct islands in the array.


Example 1:
Input: 
[
 [1,1,1,1,1],
 [1,0,0,0,0],
 [0,0,0,0,1],
 [1,1,0,0,1]
]

Output: 3

Explanation: There are three islands islands in the array above. Each of the three islands are distinct.

Example 2:
Input: 
[
 [1,1,1,1,1],
 [0,0,0,0,0],
 [0,0,0,0,0],
 [1,1,1,1,1]
]

Output: 1

Explanation: There are two islands islands in the array above. However, they are not distinct (one island can be translated vertically to obtain the other - intuitively they represent the same "signature").

Constraints:
The elements in the input matrix will only be either 0 or 1
"""


class Solution:
    def __init__(self):
        # These two lists are used to make our recursive calls neater
        self.d_row = [-1, 0, 0, 1]
        self.d_col = [0, -1, 1, 0]

    def numberOfDistinctIslands(self, grid):
        """
        Interface
        ----
        :type grid: list of list of int
        :rtype: int

        Approach
        ----
        1. First, let's see how to count the number of islands without considering whether the islands are distinct. 

        2. This can be done using a straightforward recursive depth-first search algorithm in which we explore an entire block of ones upon reaching a single "1". 

        3. As we visit each block, we make sure to flag the position as "visited" so that we do not visit it again. 
        This can be done by changing the position's value from "1" to any other value. 

        4. Now, we just need to figure out how many of the islands we visit are distinct. This can be done by using the fact that two islands are distinct if and only if the order
        in which our two depth-first search algorithms change directions and backtracks while traversing the two islands are different.

        5. For example, if our depth-first search traversal goes left, down, and right (in that order), then the shape of the island produced from this traversal will be different than 
        if we were to instead go left, down, and down. While one may think that "left, down, right" is equivalent to "left, up, right", the latter case is not possible since we are searching from islands from top to bottom. 

        6. In other words, the uniqueness of our depth-first search traversal is guaranteed by the fact that our depth-first search "prioritizes" one order over all others.
        Therefore, we can construct a "signature" for each depth-first search that we start. Each signature is a string consisting of our entire path, and it is constructed on-the-fly as we perform the traversal. 
        Since each signature corresponds to a unique island shape, we can store them all in a set and return the set's size as our final answer.

        Complexity
        ----
        Time : O()
        Space : O()
        """
        islands = set()

        # Call the flood_fill function each time 1 is encountered
        for row in range(0, len(grid)):
            for col in range(0, len(grid[row])):
                if grid[row][col] == 1:
                    signature = []
                    self.flood_fill(grid, signature, row, col)
                    # Add signature to the HashSet
                    islands.add(tuple(signature))

        # Size of the HashSet is unique islands encountered
        return len(islands)

    # Helper function for calculating the answer recursively
    def flood_fill(self, grid, signature, row, col):
        # Flag the position as water so that we don't revisit it.
        grid[row][col] = 0

        # We check if the cell is in bounds & if it is a 1
        for i in range(0, 4):
            new_row = row + self.d_row[i]
            new_col = col + self.d_col[i]

            if (
                self.is_in_bounds(grid, new_row, new_col) and
                grid[new_row][new_col] == 1
            ):
                signature.append(i)
                self.flood_fill(grid, signature, new_row, new_col)

        # Adding -1 to the signature tells that it has changed direction and backtracks
        signature.append(-1)

    # Helper function to check if the co-ordinates are valid
    def is_in_bounds(self, grid, row, col):
        return row >= 0 and col >= 0 and row < len(grid) and col < len(grid[row])


islands = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [1, 1, 0, 0, 1]
]

s = Solution()
print(s.numberOfDistinctIslands(islands))
