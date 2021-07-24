"""
Rules
1. Each column and row in a can only have numbers from 1-9 once 
2. Each box can only contain numbers from 1-9 

Strings for identification
v = value
1. r(v)
2. (v)c
3. r(v)c

r and c only range from 0-2

Input clarification
[[1,2,0,3,5,0,0,0,7]]
..
..
..
[[4,0,0,2,1,0,0,0,9]]
"""

from typing import List


class Solution:
    def validSudoku(self, board: List[List[int]]) -> bool:
        """
        input
        ----
        board: list of lists of integers
        output
        ----
        bool indicating whether or not the placement is a valid sudoku

        Complexity
        ----
        We know the size of our input
        Time : O(1)
        Space : O(1)
        """
        seen = {}
        for r in range(0, 9):
            for c in range(0, 9):
                v = board[r][c]
                if v != 0:
                    # create the row col and box strings
                    row = f'{r}({v})'
                    col = f'({v}){c}'
                    box = f'{r // 3}({v}){c // 3}'

                    if row in seen or box in seen or col in seen:
                        return False

                    seen[row] = True
                    seen[col] = True
                    seen[box] = True

        return True
