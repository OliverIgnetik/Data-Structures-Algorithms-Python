from general_graph import AdjacencyListGraph
from math import inf
################################# Bellman Ford Algorithm in Python ################################
# RESOURCES
# https://www.youtube.com/watch?v=lyw4FaxrwHg&list=PLDV1Zeh2NRsDGO4--qE8yH72HFL1Km93P&index=20
# https://www.youtube.com/watch?v=vzBtJOdoRy8

# Bellman Ford algorithm helps us find the shortest path from a vertex
# to all other vertices of a weighted graph.
# NOTE: It is similar to Dijkstra's algorithm but it can work with graphs in which edges can have negative weights.

################################# Time Complexity ################################
# The time complexity is on the order of O(EV). If the graph as no edges with negative
# edges then it is better Dijkstra's algorithm

################################# Space Complexity ################################
# And, the space complexity is O(V)

################################ Applications ################################
# 1. For calculating shortest paths in routing algorithms
# 2. For finding the shortest path
# 3. Performing an arbitrage between two or more markets

################################ IMPLEMENTATION ################################
# Let E be the number of Edges
# Let V be the number of Vertices
# Let S be the id of the starting node
# Let D be an array of size V that tracks the best distance from S to each node


def bellman_ford(g, n, s):
    dist = [inf] * n
    dist[s] = 0

    # Cycle through every edge in the graph n times
    for _ in range(n):
        for i in range(n):
            for edge in g[i]:
                if (dist[edge.f] + edge.cost < dist[edge.t]):
                    dist[edge.t] = dist[edge.f] + edge.cost

    # Run the algorithm a second time to detect which nodes are part of a negative cycle
    # If we can relax an edge there this is a negative cycle

    # NOTE: The nodes which are connected to edges that can be relaxed
    # are given the value of inf
    for _ in range(n):
        for i in range(n):
            for edge in g[i]:
                if (dist[edge.f] + edge.cost < dist[edge.t]):
                    dist[edge.t] = inf

    return dist


################################ TESTS ################################
g = AdjacencyListGraph()

g.add_edge(0, 1, 5)
g.add_edge(1, 5, 1)
g.add_edge(5, 4, 3)
g.add_edge(1, 6, 2)
g.add_edge(6, 4, 7)
g.add_edge(4, 3, 8)
g.add_edge(3, 2, 3)

start = 0
distance_to_nodes = bellman_ford(g, len(g), start)
end = 2
for node in range(len(g)):
    print('The distance to node index {:<2d}is : {:<3d} units'.format(
        node, distance_to_nodes[node]))
