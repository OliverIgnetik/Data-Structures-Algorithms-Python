"""
Check If A Graph Is Bipartite
Given a graph return true if it is bipartite, return false otherwise.

What does it mean for a graph to be bipartite?
----
In the mathematical field of graph theory, a bipartite graph (or bigraph)
is a graph whose vertices can be divided into two disjoint and independent
sets U and V such that every edge connects a vertex in U to one in V. Vertex
sets U and V are usually called the parts of the graph. Equivalently, a 
bipartite graph is a graph that does not contain any odd-length cycles.

The two sets U and V may be thought of as a coloring of the graph with two colors:
if one colors all nodes in U blue, and all nodes in V green, each edge has endpoints
of differing colors, as is required in the graph coloring problem.
In contrast, such a coloring is impossible in the case of a non-bipartite graph,
such as a triangle: after one node is colored blue and another green, the third vertex
of the triangle is connected to vertices of both colors, preventing it from being assigned
either color.

Intuition
----
For every edge the associated nodes are in different groups/colour groups.

Example 1:
Input:
[
  [3],
  [3],
  [4],
  [],
  [],
]

Output: true
Explanation: This graph can be bipartitioned such that there are no internal connections within the bipartition.

3  <- 1    2 -> 4
^
|
0
"""
from collections import deque


class Solution:
    def isBipartite(self, adjList):
        """
        :type adjList: list of list of int
        :rtype: bool

        Approach
        ---- 
        NOTE: For each edge the associated nodes must be different colours
        1. Use BFS to place each node in seperate sets A and B.
        2. Check that:
            - A union B = V
            - A intersection B = Null Set
        3. If these conditions are met then we have a bipartite graph

        NOTE: this does not assume we are dealing with a strongly connected graph

        Complexity
        ----
        Time : O(E + V)
        Space : O(V)

        Application
        ----
        Given N gears that can rotate clockwise/counter-clockwise. 
        Question: will the gears be able to rotate?
        Answer: If the graph is bipartite it will rotate. If not the gears will break.

        ie. if one gear rotates clockwise, every gear it touches must rotate 
        counter clockwise for the machine to work.
        """
        # Set up two groups for bipartition
        groups = [-1] * len(adjList)

        # We need to keep check of what nodes we have visited
        seen = set()
        q = deque()

        for i in range(len(adjList)):
            if (i not in seen):
                # Start BFS on this node
                q.append(i)
                while len(q) != 0:
                    curr_node = q.popleft()
                    # check if we have seen this node
                    if curr_node not in seen:
                        seen.add(curr_node)
                        # case of first node in a section of the graph
                        if groups[curr_node] == -1:
                            groups[curr_node] = 1
                        for neigbour in adjList[curr_node]:
                            # if we have seen the neighbour then skip
                            if neigbour in seen:
                                continue
                            # If the colour of the current node is the same then we can not have a bipartite graph
                            if groups[neigbour] == groups[curr_node]:
                                return False
                            if groups[neigbour] == -1:
                                # set the neighbour to the opposite group to satisfy the bipartition property
                                groups[neigbour] = int(not groups[curr_node])
                            # add neighbour to queue
                            q.append(neigbour)
        return True


g_adj_list = [
    [3],
    [3],
    [4],
    [],
    [],
]

print(Solution().isBipartite(g_adj_list))
