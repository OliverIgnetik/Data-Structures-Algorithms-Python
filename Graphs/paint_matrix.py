"""
Paint A Matrix
Given a 2-color matrix and a point start, flip all points in the connected region of start node to the opposite color.

Example:
Input:
image = [
  [0, 0, 1, 0],
  [0, 0, 1, 0],
  [0, 0, 1, 0],
  [0, 0, 1, 0]
]
row = 0
col = 1
newColor = 1

Output:
[
  [1, 1, 1, 0],
  [1, 1, 1, 0],
  [1, 1, 1, 0],
  [1, 1, 1, 0],
]

Explanation: (0, 1) is color 0, the whole adjacent region was flipped to 1's
"""
from collections import deque


class Solution:
    def paint(self, image, row, col, newColor):
        '''
        :type image: list of list of int
        :type row: int
        :type col: int
        :type newColor: int
        :rtype: list of list of int

        Approach 
        ----
        Use BFS to traverse every cell in the graph 

        Complexity 
        ----
        Time : O(E + V) -> O(mn)
        Space : O(V) -> O(mn)
        '''
        total_rows = len(image)
        total_cols = len(image[0])

        # initiliaze variables
        seen = set()
        queue = deque()
        queue.append([row, col])

        while len(queue) != 0:
            row, col = queue.popleft()
            signature = str(row) + str(col)
            if signature not in seen:
                if image[row][col] != newColor:
                    image[row][col] = newColor
                seen.add(signature)
                # process the neighbours
                new_coords = [[row + 1, col], [row - 1, col],
                              [row, col + 1], [row, col - 1]]
                for new_coord in new_coords:
                    new_row, new_col = new_coord[0], new_coord[1]
                    if new_row >= 0 and new_row < total_rows and new_col >= 0 and new_col < total_cols:
                        signature = str(new_row) + str(new_col)
                        if image[new_row][new_col] != newColor and signature not in seen:
                            queue.append([new_row, new_col])

        return image
