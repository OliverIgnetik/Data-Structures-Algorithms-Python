"""
References
Pg. 221 EPI Python
https://www.youtube.com/watch?v=kX5frmc6B7c&t=702s CSBreakDown
https://www.youtube.com/watch?v=wGbuCyNpxIg BackToBackSWE
https://www.youtube.com/watch?v=jPcBU0Z2Hj8 Numberphile

NOTES
Inputs
N(int) = number of queens and number of rows and columns of chessboard

Outputs
result(list of lists) = placements for N queens

Key Point
-------------------------------------------------
Test if a newly placed queen will conflict any earlier queens
placed before it(ie. up to an index in col_placement equal to the current row)

A queen lies on a line of attack if:

Our algorithm avoids this case by construction
R_1 = R_2 SAME ROW


We need to ensure the following constraints are respected in our algorithm
C_1 = C_2 SAME COLUMN
|R_1 - R_2 | = | C_1 - C_2 | DIAGONAL

NOTE: We go through row by row to find a column to place a queen that is safe.
"""


"""
The N Queens Problem
Given an input integer n, generate all n x n boards with n non - attacking queens placed.

A queen q1 is "attacking" another queen q2 if;
q2 sits in the same row as q1
q2 sits in the same column as q1
q2 sits in the diagonal reach of q1

Attacking Arrangement:
[
 "-Q--",
 "-Q--",
 "Q---",
 "--Q-"
]

Explanation:
- Queen in row 0 is attacking queen in row 1 column - wise.
- Queen in row 2 is attacking queen in row 1 diagonally.

Example:
Input: 4

Output:
[
 [
  "-Q--",
  "---Q",
  "Q---",
  "--Q-"
 ],
 [
  "--Q-",
  "Q---",
  "---Q",
  "-Q--"
 ]
]


Explanation: There are only 2 4x4 board arrangements of 4 non - attacking queens

Constraints:
1 <= n <= 10
"""
from typing import List

################################### EPI IMPLEMENTATION ###################################


def n_queens(n: int) -> List[List[int]]:
    def solve_n_queens(row):
        if row == n:  # THE GOAL
            # All queens are legally placed.
            result.append(col_placement.copy())
            return
        for col in range(n):
            """
            CONFLICTS HAPPEN WHEN
            - abs(c - col) = 0 (VERTICAL)
            - abs(c - col) = row - i(DIAGONAL)

            NOTE: enumerate(col_placement[:row])
            the index i is the row
            the value c is the column
            """
            if all(
                    abs(c - col) not in (0, row - i)
                    for i, c in enumerate(col_placement[:row])):
                # if there are no conflicts with any of the placements then we can proceed
                col_placement[row] = col
                # increment the row value to place the next queen
                solve_n_queens(row + 1)

    result: List[List[int]] = []
    col_placement = [0] * n
    solve_n_queens(0)
    return result


print(n_queens(4))

################################### BACKTOBACKSWE IMPLEMENTATION ###################################


class Solution:
    def solveNQueens(self, n):
        """
        Interface
        ----
        :type n: int
        :rtype: list of list of str

        Approach
        ----
        1. Identify decision space at each recursive call, the state we must pass along and our goal
        - state : placements, row we are on 

        2. Identify constraints 
        Our algorithm avoids this case by construction
        R_1 = R_2 SAME ROW
        We need to ensure the following constraints are respected in our algorithm
        C_1 = C_2 SAME COLUMN
        |R_1 - R_2 | = | C_1 - C_2 | DIAGONAL

        3. Identify when to backtrack 

        Complexity
        ----
        Naive bounding 
        Branching factor = N
        Depth = N 

        Time : O(N^N)
        Space : O(N)
        """
        results = []

        self.solve(0, n, [], results)

        return results

    def solve(self, row, n, col_placements, results):
        """
        NOTE: BASECASE
        All n queens have been placed in the n rows. We have
        reached the bottom of our recursion. We can now add
        the colPlacements to the results.
        """
        if row == n:
            results.append(
                self.generate_board_from_placements(col_placements, n))
            return

        """
        Try all columns in the current row that we are making
        a choice on.

        The colPlacements list will hold the column we place a
        queen for the i'th row.

        So if I have [ 1, 3, 0, 2 ] that means:

        It is a 4 x 4 board.

        row index 0 has a queen placed in column index 1
        row index 1 has a queen placed in column index 3
        row index 2 has a queen placed in column index 0
        row index 3 has a queen placed in column index 2
        """
        for col in range(0, n):

            # Record a column placement for this row
            # NOTE: STATE
            col_placements.append(col)

            """
            NOTE: RECURSION
            If it is a valid placement we recurse to work on
            the next row (row + 1) in a recursive call
            """
            # NOTE: CONSTRAINT
            if self.is_valid(col_placements):
                # Explore
                self.solve(row + 1, n, col_placements, results)

            """
            NOTE: BACKTRACK
            We are done exploring with that placement and now we
            will remove it from our colPlacements. We will loop
            back around and try more column placements for this
            row (if there are any left)
            """
            col_placements.pop()

    # NOTE: CONSTRAINT DEFINITION IS THE HARDEST PART OF THIS PROBLEM
    # Check if a column placement that we just put in the colPlacements
    # list is actually valid to recurse on
    def is_valid(self, col_placements):

        # rowWeAreValidatingOn is the row that we just placed a queen on
        # and we need to validate the placement
        row_we_are_validating_on = len(col_placements) - 1

        # Loop and check our placements in every row previous against
        # the placement that we just made
        for ith_queen_row in range(0, row_we_are_validating_on):

            """
            Get the absolute difference between:

            1.) The column of the already placed queen we are comparing against -> colPlacements.get(ithQueenRow)

            2.) The column of the queen we just placed -> colPlacements.get(rowWeAreValidatingOn)
            """
            absolute_column_distance = abs(
                col_placements[ith_queen_row] -
                col_placements[row_we_are_validating_on]
            )

            """
            1.) absoluteColumnDistance == 0
                If the absolute difference in columns is 0 then we placed in a column being
                attacked by the i'th queen.

            2.) absoluteColumnDistance == rowDistance
                If the absolute difference in columns equals the distance in rows from the
                i'th queen we placed, then the queen we just placed is attacked diagonally.

            For Constraint #2 imagine this:

            [
                "--Q-",  <--- row 0 (Queen 1)
                "Q---",  <--- row 1 (Queen 2)
                "-Q--",  <--- row 2 (Queen 3)
                "----"
            ]

            1.) 
                Absolute Column Distance Between Queen 2 & 3 == 1.
                Queen 2 is in col 0, Queen 3 is in col 1. 1 - 0 = 1.

            2.)
                Absolute Row Distance Between Queen 2 & 3 == 1
                Queen 2 is in row 1, Queen 3 is in row 2. 2 - 1 = 1.
            """
            # NOTE: row_we_are_validating_on will be greater then everything else
            row_distance = row_we_are_validating_on - ith_queen_row

            if (
                absolute_column_distance == 0 or
                absolute_column_distance == row_distance
            ):
                return False

        return True

    def generate_board_from_placements(self, col_placements, n):
        board = []
        total_items_placed = len(col_placements)

        # Materialize a row for each queen that we placed
        for row in range(0, total_items_placed):
            s = ""

            for col in range(0, n):
                if col == col_placements[row]:
                    s += 'Q'
                else:
                    s += '-'
            # Add the row to the board
            board.append(s)

        return board


s = Solution()
placements = s.solveNQueens(8)
print(s.generate_board_from_placements(placements))
