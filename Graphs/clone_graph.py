"""
Clone A Graph
Given an undirected graph represented as an adjacency list, return a deep clone of the graph.

  0
 / \
1 - 10
"""

from collections import deque


class GraphVertex:
    def __init__(self, val):
        self.val = val
        self.adjacents = []

    def __repr__(self):
        return f'{self.__class__.__name__}({self.val}, {[vertex.val for vertex in self.adjacents]})'


class Solution:
    def cloneGraph(self, start: GraphVertex):
        """
        Inputs
        ----
        start : GraphVertex object

        Outputs
        ----
        clone_start : GraphVertex object

        Approach
        ----
        1. Perform BFS
        2. Use a hashmap to take note of mappings


        Complexity
        ----
        Time : O(V + E)
        Space : O(V)
        """
        clone_mappings = {}
        q = deque()
        q.append(start)
        clone_mappings[start.val] = GraphVertex(start.val)
        visited = set()

        while len(q) != 0:
            # poll the queue
            vertex = q.popleft()
            # grab the current value and adjacents
            cur_value, adjacents = vertex.val, vertex.adjacents
            # if we haven't seen the current node process it
            if cur_value not in visited:
                visited.add(cur_value)
                # iterate over the neighbours
                for neighbour in adjacents:
                    neighbour_value = neighbour.val
                    # if we haven't visited this neighbour
                    # add it to the queue
                    if neighbour_value not in visited:
                        q.append(neighbour)
                        # create the clone for the neighbour
                        # if it's not yet in the clone_mappings
                        if neighbour_value not in clone_mappings:
                            clone_mappings[neighbour_value] = GraphVertex(
                                neighbour_value)

                    # update the adjacents for the curr_node
                    clone_mappings[cur_value].adjacents.append(
                        clone_mappings[neighbour_value])

        return clone_mappings[start.val]


# adjacency list representation
node0 = GraphVertex(0)
node1 = GraphVertex(1)
node10 = GraphVertex(10)

node0.adjacents = [node1, node10]
node1.adjacents = [node0, node10]
node10.adjacents = [node0, node1]

"""
DRAWING OF ABOVE TEST CASE
  0
 / \
1 - 10
"""

s = Solution()
node0_clone = s.cloneGraph(node0)
print(node0_clone)
