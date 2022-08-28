"""
Search A Maze For An Exit
Given a maze with an end point end and a start point start, find a path from start to end and return that path.

Constraints:
The path must be a simple path (no points can be repeated and "retraversed")
"""


class Solution:
    def check_valid_coordinate(self, row, col):
        if row >= 0 and row < self.total_rows:
            if col >= 0 and col < self.total_cols:
                if self.maze[row][col] == 'white':
                    return True

    def get_neighbours(self, row, col):
        neighbours = [[row + 1, col], [row - 1, col],
                      [row, col + 1], [row, col - 1]]

        return neighbours

    def convert_id_to_coords(self, id):
        return (id - id % self.total_cols) // self.total_rows, id % self.total_cols

    def convert_coords_to_id(self, row, col):
        return row * self.total_cols + col

    def recursive_solver(self, row, col):
        """
        In each stack frame we check if there are any neighbours we can visit.
        If we can visit a neighbour we mark its cell as black
        """
        self.maze[row][col] = 'black'

        # this is our goal
        if self.convert_coords_to_id(row, col) == self.end:
            return True

        # get all the neighbours
        neighbours = self.get_neighbours(row, col)
        for neighbour in neighbours:
            neighbour_row, neighbour_col = neighbour
            # if it's not valid then skip it
            if not self.check_valid_coordinate(neighbour_row, neighbour_col):
                continue
            # if it is valid then explore for potential solution
            neighbour_id = self.convert_coords_to_id(
                neighbour_row, neighbour_col)
            # append the neighbour id to path
            self.path.append(neighbour_id)
            if self.recursive_solver(neighbour_row, neighbour_col):
                return True
        # if we can't find a solution after exhausting all neighbours
        # NOTE: backtrack
        self.path.pop()
        self.maze[row][col] = 'white'
        return False

    def maze_solver(self, maze, start, end):
        """
        Assumptions
        ----
        We assume start and end are given as integers with the maze cells numbered as follows

        maze = [[0, 1, 2, 3, 4], 
                [5, 6, 7, 8, 9]
                ...]

        Approach 
        ---- 
        Make use of recursive DFS

        Complexity
        ----
        Time : O(E + V) -> O(RowsxColumns)
        Space : O(V) -> O(RowsxColumuns)
        """
        self.path = []

        self.total_rows = len(maze)
        self.total_cols = len(maze[0])
        self.maze = maze
        self.start = start
        self.end = end

        start_row, start_col = self.convert_id_to_coords(self.start)
        end_row, end_col = self.convert_id_to_coords(self.end)

        if not self.check_valid_coordinate(start_row, start_col) or not self.check_valid_coordinate(end_row, end_col):
            raise ValueError(
                f'{self.start} and {self.end} must be placed on white squares and inside the board')

        self.path.append(start)
        self.recursive_solver(start_row, start_col)
        return self.path


maze = [['white', 'white', 'white', 'black', 'white'],
        ['white', 'black', 'white', 'black', 'white'],
        ['white', 'black', 'white', 'black', 'white'],
        ['black', 'white', 'white', 'white', 'white'],
        ['white', 'white', 'black', 'black', 'white']]

s = Solution()

print(s.maze_solver(maze, 20, 4))
