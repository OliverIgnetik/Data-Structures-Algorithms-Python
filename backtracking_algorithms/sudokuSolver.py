"""
Implement A Sudoku Solver
Given a partially solved sudoku board solve the sudoku puzzle and return the complete board.

Sudoku is a puzzle game where a player places numbers 1 to n on an n x n board in an arrangement that follows 3 constraints:
- Column Constraint: A number cannot repeat in a column
- Row Constraint: A number cannot repeat in a row
- Subgrid Constraint: A number cannot repeat in a subgrid

Example (Same as above):
Input:
[
  ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
  ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
  ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
  ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
  ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
  ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
  ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
  ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
  ['.', '.', '.', '.', '8', '.', '.', '7', '9']
]

Output:
[
  ['5', '3', '4', '6', '7', '8', '9', '1', '2'],
  ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
  ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
  ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
  ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
  ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
  ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
  ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
  ['3', '4', '5', '2', '8', '6', '1', '7', '9']
]

Constraints:
n = 9 always (the board is always 9 x 9)
The board will always be solvable
"""

import math


class Solution:
    EMPTY_ENTRY = "."

    def solveSudoku(self, board):
        """
        Interface 
        ----
        :type board: list of list of str
        :rtype: list of list of str

        Approach
        ----

        1. Goal : Fill every cell 

        2. Constraints, Decision Space and State : what choices do we have at each stack frame?
        - check the row, col and subgrid constraint to inform decision space (ie. choice of number for current state)
        - we have to pass the current col, row and board data as state

        3. Backtracking : when do we reach an exhausted decision space? 

        Complexity
        ----
        For a 9x9 board
        Time : O(1)
        Space : O(1)

        For a NxN board
        Branching factor = N ie. at each step we can make N choices
        Depth = N^2 ie. the depth is the size of the board

        Time : Superexponential O(N^(N^2))
        Space : O(N^2) just counting the call stack depth
        """
        self.solved_from_cell(0, 0, board)

        return board

    # Helper function for calculating and filling the board
    def solved_from_cell(self, row, col, board):
        # NOTE: BASE CASES
        # we have reached the end of the column
        if col == len(board[row]):
            col = 0
            row += 1

            # if we have reached the last cell we are done
            if (row == len(board)):
                return True

        # Entry already filled out
        # NOTE: CONSTRAINTS move onto the next cell
        if board[row][col] != Solution.EMPTY_ENTRY:
            return self.solved_from_cell(row, col + 1, board)

        # NOTE: DECISION SPACE set of numbers
        for i in range(1, len(board) + 1):
            char_to_place = str(i)

            # NOTE: 3 CONSTRAINTS : column, row and subgrid
            if self.can_place_value(board, row, col, char_to_place):
                # Choose
                board[row][col] = char_to_place

                # Explore: Can we solve the path from the next cell?
                if self.solved_from_cell(row, col + 1, board):
                    return True

                # NOTE: Backtracking on our decision and try the next number
                board[row][col] = Solution.EMPTY_ENTRY

        # Could not fill board cell [row][col]
        return False

    # Helper function to check if character can be placed at a particular index
    def can_place_value(self, board, row, col, char_to_place):
        # NOTE: COLUMN CONSTRAINT
        # Check column of placement
        for placement_row in board:
            if char_to_place == placement_row[col]:
                return False

        # NOTE: ROW CONSTRAINT
        # Use `column` to prevent overlap with `col` parameter
        for column in range(0, len(board[row])):
            if char_to_place == board[row][column]:
                return False

        # NOTE: SUBGRID CONSTRAINT
        # Check subgrid
        region_size = int(math.floor(math.sqrt(len(board))))

        # rows = (0, 1, 2) -> (0), rows = (3, 4, 5) -> (1), rows = (6, 7, 8) -> (2)
        vertical_box_index = row // region_size
        horizontal_box_index = col // region_size

        # (subbox_row, subbox_col) = (2,2) -> (i, j) = (6,6)
        top_left_of_subbox_row = region_size * vertical_box_index
        top_left_of_subbox_col = region_size * horizontal_box_index

        # scan the subgrid for an occurence of this char
        for i in range(0, region_size):
            for j in range(0, region_size):
                if (
                    char_to_place ==
                    board[top_left_of_subbox_row +
                          i][top_left_of_subbox_col + j]
                ):
                    return False

        return True


board = [
    ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
    ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
    ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
    ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
    ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
    ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
    ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
    ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
    ['.', '.', '.', '.', '8', '.', '.', '7', '9']
]

sn = Solution()
print(sn.solveSudoku(board))
