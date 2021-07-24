"""
Topological Sorting
Given a directed graph return a valid topological ordering of the vertices.

A "topological ordering" is an ordering of the vertices of the graph such that for all edges(u, v) in the graph, node u comes before node v in the ordering.

Example:
Input:
        1 -> 2
        |    |
        ˅    ˅
        3 -> 4

Edges
{u,v}
----
{1,2}
{1,3}
{3,4}
{2,4}

Indegree
----
1 : 0
2 : 1
3 : 1
4 : 2

All the u (tails) come before v(heads)
Output: [1, 2, 3, 4]

Explanation:
There are actually two valid topological orderings here:
1. [1, 2, 3, 4]
2. [1, 3, 2, 4]
"""
from typing import List


class Solution:
    def calculate_indegrees(self) -> List[int]:
        indegrees = {}
        for node in self.graph:
            if node not in indegrees:
                indegrees[node] = 0
            neighbours = self.graph[node]
            for neighbour in neighbours:
                if neighbour in indegrees:
                    indegrees[neighbour] += 1
                else:
                    indegrees[neighbour] = 1

        return indegrees

    def topological_sort(self, graph: List[List[int]]) -> List[int]:
        """
        Inputs
        ----
        graph : list of list of integers (adjacency list representation)

        Outputs
        ----
        ordering : list of integers detailing topological orderings

        Approach
        ----
        We think of an edge as: 
        {u , v}
        Where u = tail and v = head

        NOTE: KEY INTUITION 
        Every single u is before v in the topological ordering

        How do we build the ordering?
        ----
        We use the indegree each node build the ordering. 

        THEOREM 
        ----
        Every DAG (Directed Acyclic Graph) has a topological ordering

        Complexity
        ----
        Time : O(V)
        Space : O(V)

        Applications 
        ----
        1. Sorting interdependant tasks by importance
        2. Task scheduling problems
        """
        self.graph = graph
        self.indegrees = self.calculate_indegrees()
        ordering = []
        s = set()
        for node in self.graph:
            # only nodes with an indegree of zero can be added to the set
            if self.indegrees[node] == 0:
                s.add(node)

        while len(s) != 0:
            # it doesn't matter which node we poll from the data structure
            node = s.pop()
            ordering.append(node)
            for neighbour in self.graph[node]:
                # we have to remove one edge
                self.indegrees[neighbour] -= 1
                if self.indegrees[neighbour] == 0:
                    s.add(neighbour)

        return ordering


graph = {
    1: [2, 3],
    2: [4],
    3: [4],
    4: []
}

s = Solution()
print(s.topological_sort(graph))
