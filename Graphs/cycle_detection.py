"""
Detect A Cycle In A Graph (Deadlock Detection)
Given a directed graph determine if it contains a cycle.

A directed graph has a cycle if we cycle back to a node that 
we have already seen. 

Using DFS is more appropriate because we want to deeply explore 
different paths

Approaches 
----
1. We can use a recursive type function similar to the maze search 
problem. This solution seems to be the more efficient, as you are not
duplicating work.
2. Just perform DFS on every node and check for a cycle

Constraints:
|V| <= 100
"""


class StackSolution:
    def __init__(self, graph):
        self.graph = graph

    def cycle_detection(self):
        """
        Complexity 
        ----
        Time : O(V(E + V))
        Space : O(V)
        """
        # go through every node in the graph
        cycle = False
        for node in self.graph:
            # check for cycle
            cycle = self.dfs_cycle_check(node)
            if cycle:
                return cycle
        return cycle

    def dfs_cycle_check(self, start):
        stack = [(start, [start])]
        while stack:
            (vertex, path) = stack.pop()
            for nxt in self.graph[vertex]:
                if nxt in set(path):
                    return True
                else:
                    stack.append((nxt, path + [nxt]))
        return False


class RecursiveSolution:
    def __init__(self, graph):
        self.graph = graph

    def detect_cycle(self) -> bool:
        """
        Approach 
        ----
        1. Each node starts as unvisited 
        2. Process each node 
        3. If we reach a node that has reachable neighbours that are 'grey' 
        we return True
        4. If the node has only neighbours with 'black' then we have exhausted the current search space

        Compexity
        ---- 
        Time : O(E + V)
        Space : O(V)

        Encoding
        ----
        'grey' - 'currently investigating'
        'black' - 'investigated'
        'white' - unvisited
        """
        self.node_status = {nkey: "white" for nkey in self.graph}

        cycle_found = False
        for node in self.graph:
            cycle_found = self.recursive_dfs(node, cycle_found)
            if cycle_found:
                break
        return cycle_found

    def recursive_dfs(self, node, cycle_found):
        if self.node_status[node] == 'black':
            return cycle_found
        # mark this node as currently investigating
        self.node_status[node] = 'grey'
        for neighbour in self.graph[node]:
            # if a neighbour has node_status with grey
            # we have found a cycle
            if self.node_status[neighbour] == 'grey':
                cycle_found = True
                return cycle_found
            if self.node_status[neighbour] == 'white':
                return self.recursive_dfs(neighbour, cycle_found)

        # if there are no neighbours that we can visit then we have exhausted this part of the search space
        self.node_status[node] = 'black'
        return cycle_found


# adjacency list for a digraph that is not connected
graph = {'A': set(['B']),
         'B': set(['C']),
         'C': set(['A']),
         'D': set(['E', 'F']),
         'E': set(['G']),
         'F': set(),
         'G': set(),
         }

s1 = StackSolution(graph)
s2 = RecursiveSolution(graph)

print(s1.cycle_detection())
print(s1.dfs_cycle_check('D'))

print(s2.detect_cycle())
