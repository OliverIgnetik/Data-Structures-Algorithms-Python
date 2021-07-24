"""
Testing Strong Connectivity
Given a directed graph determine if it is strongly connected. Return true if it is, otherwise return false.

NOTE: CONNECTIVITY REQUIREMENTS
A directed graph is weakly connected if all vertices are reachable when all edges are interpreted as undirected. 
Remember we can represent an undirected edge as two directed edges

A directed graph is strongly connected if for all possible vertices u there is a path to any other vertex v and there is a path from that v back to the original u.

Example 1:
Input:
        1
        |
        ˅
        2

Output: false
Explanation: This graph is weakly connected, but not strongly connected. There is a path from 1 to 2, but not from 2 to 1.

Example 2:
Input:
        1 <- 4
        |    ^
        ˅    |
        2 -> 3

Output: true
Explanation:
| u | v | u -> v | v -> u |
| 1 | 2 |  true  |  true  |
| 1 | 3 |  true  |  true  |
| 1 | 4 |  true  |  true  |
| 2 | 3 |  true  |  true  |
| 2 | 4 |  true  |  true  |
| 3 | 4 |  true  |  true  |
"""
from typing import List
from collections import deque


class BruteForceSolution:
    def bfs_scan(self, start: int) -> bool:
        all_nodes = set(range(len(self.graph)))
        visited = set()
        q = deque()
        q.append(start)
        while len(q) != 0:
            node = q.popleft()
            if node not in visited:
                visited.add(node)
                for neighbour in self.graph[node]:
                    if neighbour not in visited:
                        q.append(neighbour)

        return all_nodes == visited

    def strongConnectivity(self, graph: List[List[int]]) -> bool:
        """
        Approach
        ----
        Perform BFS on every node and make sure that we can
        reach every node in the graph 
        If we can reach every node from every other node then we 
        have a strongly connected graph

        Complexity 
        ----
        Time : O(V(E+V))
        Space : O(V)
        """
        self.graph = graph
        node_index = 0
        strongConnectivity = True
        while node_index < len(self.graph) and strongConnectivity:
            strongConnectivity = self.bfs_scan(node_index)
            node_index += 1
        return strongConnectivity


class OptimizedSolution:
    def bfs_scan(self, start: int) -> bool:
        all_nodes = set(range(len(self.graph)))
        visited = set()
        q = deque()
        q.append(start)
        while len(q) != 0:
            node = q.popleft()
            if node not in visited:
                visited.add(node)
                for neighbour in self.graph[node]:
                    if neighbour not in visited:
                        q.append(neighbour)

        return all_nodes == visited

    def reverseGraph(self):
        # we need to make a new graph structure
        new_graph = [[] for _ in range(len(self.graph))]
        # go through every node
        for node in range(len(self.graph)):
            # for each of its neighbours append the current node to the adjacency list
            for neighbour in self.graph[node]:
                new_graph[neighbour].append(node)
        self.graph = new_graph

    def strongConnectivity(self, graph: List[List[int]]) -> bool:
        """
        Approach
        ----
        Perform BFS on every node and make sure that we can
        reach every node in the graph 
        If we can reach every node from every other node then we 
        have a strongly connected graph

        NOTE: (everyone node which reach 0) - (0) - (every node 0 can reach)

        Therefore every node can reach every other node and vice versa

        Complexity 
        ----
        Time : O((E+V))
        Space : O(V)
        """
        self.graph = graph
        if not self.bfs_scan(0):
            return False
        self.reverseGraph()
        return self.bfs_scan(0)


g = [[1],
     [2],
     [3, 4],
     [0],
     [2]
     ]
s1 = BruteForceSolution()
s2 = OptimizedSolution()

print(s1.strongConnectivity(g))
print(s2.strongConnectivity(g))
