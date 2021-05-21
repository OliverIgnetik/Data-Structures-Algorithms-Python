import sys
sys.path.append('..\\..\\Data Structures - Trees\\heaps')

from math import inf
from typing import NamedTuple
from dary_heap import minIndexedDHeap
from directed_graph import AdjacencyListGraph

################### DATA STRUCTURES ##############################
# Resources
# https://www.youtube.com/watch?v=pSqmAO-m7Lk   WilliamFiset Dijkstra's algorithm

############### Optimal D-ary Heap ###############
# A D-ary heap is a heap variant in which each node has D children.
# The state of the art methods use D-ary heaps which reduce the cost of
# decreaseKey operations by increasing the cost of removal operations
# compared to an Indexed Priority Queue. Removal operations are much less common in dense graphs.

# The best degree, D, to use is D = E/V to balance removals against decreaseKey operations
# improving the time complexity to :
# O(E*log_{E/V}(V))


##################### ALGORITHM IMPLEMENTATION ###############
# In the PQ used in the lazy algorithm it's more efficient to insert a new
# key-value pair in O(logN) then it is to update an existing key's value

# This is inefficient for dense graphs because we end up with several stale
# outdated key-value pairs in our PQ. The eager version avoids duplicate key-value
# pairs by O(logN) updates using an min D-ary heap.
def dijkstra_dary_heap(g, n, s):
    vis = [0] * n
    dist = [inf] * n
    dist[s] = 0
    prev = [None] * n

    degree = g.num_edges / g.num_vertices
    ipq = minIndexedDHeap(degree, n)
    ipq.insert(s, 0)

    while ipq.size != 0:
        nodeId = ipq.peekMinKeyIndex()
        vis[nodeId] = 1
        minValue = ipq.pollMinValue()

        # if we have already visited the node then we
        # can't get a shorter path
        if (minValue > dist[nodeId]):
            continue

        for edge in g[nodeId]:
            if vis[edge.to]:
                continue
            # Relax edge by updating min cost
            newDist = dist[nodeId] + edge.cost
            if newDist < dist[edge.to]:
                prev[edge.to] = nodeId
                dist[edge.to] = newDist
                if edge.to not in ipq:
                    ipq.insert(edge.to, newDist)
                else:
                    ipq.decrease(edge.to, newDist)
    return dist


###################################### TESTS ##########################################
g = AdjacencyListGraph()

g.add_edge(0, 1, 5)
g.add_edge(1, 5, 1)
g.add_edge(1, 6, 2)
g.add_edge(3, 2, 3)
g.add_edge(4, 3, 8)
g.add_edge(4, 1, 2)
g.add_edge(4, 9, 2)
g.add_edge(5, 4, 3)
g.add_edge(6, 7, 3)
g.add_edge(6, 8, 2)
g.add_edge(7, 9, 4)
g.add_edge(8, 6, 4)
g.add_edge(9, 4, 2)
g.add_edge(9, 2, 4)
g.add_edge(9, 6, 1)

start = 0
distance_to_nodes = dijkstra_dary_heap(g, len(g), start)
end = 2
for node in range(len(g)):
    print('The distance to node index {:<2d}is : {:<3d} units'.format(
        node, distance_to_nodes[node]))

print('The distance to the target node {:<2d}is : {:<3d} units'.format(
    end, distance_to_nodes[end]))
