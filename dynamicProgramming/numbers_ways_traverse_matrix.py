"""
Number of Ways To Traverse A Matrix
Given an integer value m (rows of a matrix), and an interger value n (columns of a matrix),
return the total possible unique, simple, paths from the top-left of the matrix to the bottom-right
with restricted moves.

NOTE: You may only make one of these moves at each position:
Down 1 cell
Right 1 cell

Example:
Input: m = 3, n = 3
Output: 6
Explanation:
s -> "start"
e -> "end"
 -----------
| s | _ | _ |
| _ | _ | _ |
| _ | _ | e |
 -----------

Total unique paths to any given cell:
 -----------
| 1 | 1 | 1 |
| 1 | 2 | 3 |
| 1 | 3 | 6 |
 -----------
"""


class Solution:
    def uniquePaths(self, rows, cols):
        """
        Interface
        ----
        :type rows: int
        :type cols: int
        :rtype: int

        Approach 
        ---- 
        1. We could solve this with DFS (O(E+V) complexity) if we wanted to know the paths explicitly BUT
        we are just asked for the number of unique paths so it is more efficient to use DP
        2. We can come to a cell from above and to the left. We need to know the total ways
        to reach a certain cell from those directions.
        3. Use DP to investigate these sub-problems

        NOTE: key insight we check how many ways you can get to the cell 
                            above                  left
        unique_paths[i,j] = unique_paths[i-1, j] + unique_paths[i, j-1] 

        Complexity
        ----
        Time : O(MN) which is better then the DFS
        Space : O(MN)
        """
        unique_paths_to_position = [[0] * cols] * rows

        """"
        BASE CASE : TOP ROW AND LEFT MOST COLUMN
        """
        # 1 unique way to get to left wall cells (go straight down)
        # NOTE: as soon as we go down one row we can't come back up
        for row in range(0, rows):
            unique_paths_to_position[row][0] = 1

        # 1 unique way to get to the top wall cells (go straight right)
        for col in range(0, cols):
            unique_paths_to_position[0][col] = 1

        # Unique ways to inner position is combination of unique ways coming
        # from both possible directions. This is the answer to the sub-problem of the current
        # rectangle bounded by row and col
        for row in range(1, rows):
            for col in range(1, cols):

                # Compute the unique paths comming from up and left
                unique_ways_to_above_cell = unique_paths_to_position[row - 1][col]
                unique_ways_to_left_cell = unique_paths_to_position[row][col - 1]

                # Store the sum of paths comming from up and left
                unique_paths_to_position[row][col] = unique_ways_to_above_cell + \
                    unique_ways_to_left_cell

        return unique_paths_to_position[rows - 1][cols - 1]


s = Solution()
num = s.uniquePaths(4, 3)
print(num)
