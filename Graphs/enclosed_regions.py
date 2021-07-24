"""
Compute Enclosed Regions
Given a matrix with only characters 'X' and 'O', return a matrix with all enclosed 'O's marked to an 'X'.

A region of 'O's is "enclosed" if the region does not reach an 'O' that touches any edge of the matrix. All 'O's on the edge of the matrix are safe from being marked to an 'X'.

Example 1:
Input:
[
    ['O', 'O'],
    ['O', 'O']
]

Output:
[
    ['O', 'O'],
    ['O', 'O']
]

Explanation: All O's touch the edge of the matrix and are therefore safe.

Example 2:
Input:
[
    ['X', 'X', 'O', 'X', 'X'],
    ['X', 'X', 'O', 'X', 'X'],
    ['X', 'X', 'O', 'X', 'X'],
    ['X', 'X', 'X', 'O', 'X'],
    ['X', 'X', 'O', 'X', 'X'],
    ['X', 'X', 'O', 'X', 'X']
]

Output:
[
    ['X', 'X', 'O', 'X', 'X'],
    ['X', 'X', 'O', 'X', 'X'],
    ['X', 'X', 'O', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'O', 'X', 'X'],
    ['X', 'X', 'O', 'X', 'X']
]

Explanation: The 2 regions of O's connect to O's that reach the edge so they are not enclosed regions. One of the O's did not reach the edge by being in a non-enclosed region so it became an 'X'.

Constraints:
The matrix will be m x n
2 <= m <= n <= 100
"""
from collections import deque


class Solution:
    def make_signature(self, row, col):
        return str(row) + str(col)

    def get_neighbours(self, row, col):
        neighbours = [[row + 1, col], [row - 1, col],
                      [row, col + 1], [row, col - 1]]
        valid_neighbours = [neighbour for neighbour in neighbours if self.valid_coordinate(
            neighbour[0], neighbour[1])]
        return valid_neighbours

    def valid_coordinate(self, row, col):
        if row >= 0 and row < len(self.board):
            if col >= 0 and col < len(self.board[0]):
                return True

    def computeEnclosedRegions(self, board):
        """
        :type board: list of list of str
        :rtype: list of list of str

        Approach 
        ----
        Use BFS 

        Complexity
        ----
        Time : O(E + V)
        Space : O(V)
        """
        self.board = board
        q = deque()
        q.append([0, 0])
        seen = set()

        while len(q) != 0:
            row, col = q.popleft()
            sig = self.make_signature(row, col)
            if sig not in seen:
                seen.add(sig)
                neighbours = self.get_neighbours(row, col)
                # check candidacy of node
                count = 0
                for neighbour in neighbours:
                    n_row, n_col = neighbour
                    if self.board[n_row][n_col] == 'X':
                        count += 1
                    # add neighbours to queue
                    n_sig = self.make_signature(n_row, n_col)
                    if n_sig not in seen:
                        q.append([n_row, n_col])

                # if it passes this test then mark with 'X'
                if count == 4 and board[row][col] != 'X':
                    self.board[row][col] = 'X'
        return self.board


board = [
    ['X', 'X', 'O', 'X', 'X'],
    ['X', 'X', 'O', 'X', 'X'],
    ['X', 'X', 'O', 'X', 'X'],
    ['X', 'X', 'X', 'O', 'X'],
    ['X', 'X', 'O', 'X', 'X'],
    ['X', 'X', 'O', 'X', 'X']
]
s = Solution()
print(s.computeEnclosedRegions(board))
