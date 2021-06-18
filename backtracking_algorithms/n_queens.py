from typing import List

"""
References
Pg. 221 EPI Python 
https://www.youtube.com/watch?v=kX5frmc6B7c&t=702s CSBreakDown
https://www.youtube.com/watch?v=wGbuCyNpxIg BackToBackSWE
https://www.youtube.com/watch?v=jPcBU0Z2Hj8 Numberphile

Inputs
N (int) = number of queens and number of rows and columns of chessboard 

Outputs
result (list of lists) = placements for N queens

Key Point
-------------------------------------------------
Test if a newly placed queen will conflict any earlier queens
placed before it (ie. up to an index in col_placement equal to the current row)

A queen lies on a line of attack if : 

Our algorithm avoids this case by construction
R_1 = R_2 SAME ROW 


We need to ensure the following constraints are respected in our algorithm
C_1 = C_2 SAME COLUMN
|R_1 - R_2| = |C_1 - C_2| DIAGONAL

NOTE: We go through row by row to find a column to place a queen that is safe.
"""


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
            - abs(c-col) = row - i (DIAGONAL)

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
