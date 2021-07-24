"""
Given a two-dimensional matrix with m rows and n columns (m x n matrix),
return its spiral ordering starting from the top left of the matrix (row 0, col 0).

Example 1
Input:
[
 [ 1, 2, 3],
 [ 4, 5, 6],
 [ 7, 8, 9]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2
Input:
[
  [1,2],
  [3,4],
  [5,6],
  [7,8]
]
Output: [1,2,4,6,8,7,5,3]

Approach
----
We can imagine that there are fences bounding our iteration.
If we imagine four boundaries as top right bottom and left we can change
them appropriately to traverse in a spiral.
Strategy
----
Once we traverse the top boundary we increment by 1 and then start traversing
the right boundary from where the top boundary is now currently placed.
"""


class Solution:
    def spiral_traversal(self, matrix):
        """
        Complexity
        ----
        Time : O(MxN)
        If we exclude the output
        We use constant space if we don't include the output
        The core algorithm works without this output data structure
        Space : O(1)
        """
        res = []
        # matrix dimensions
        M, N = len(matrix), len(matrix[0])
        # init fences
        top, left, right, bottom = 0, 0, N - 1, M - 1
        # you need to pay special attention to indexing
        while top <= bottom and left <= right:
            # the guards will only stop the while loop from being reentered
            # the guard top <= bottom will not stop the iteration midway
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            # we need this to stop the bottom from rereading what the top has already read
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1

            # we need this to stop left from rereading what right has already read
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res


m1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

m2 = [
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
]

m3 = [
    [15, 14, 13, 14],
    [40, 50, 60, 12],
    [30, 20, 10, 11]
]

print(Solution().spiral_traversal(m3))
