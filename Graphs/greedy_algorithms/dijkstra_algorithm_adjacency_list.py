"""
Resources
- https://www.youtube.com/watch?v=pSqmAO-m7Lk   WilliamFiset Dijkstra's algorithm
- https://www.youtube.com/watch?v=jND_WJ8r7FE&list=PLDV1Zeh2NRsB6SWUrDFW2RmDotAfPbeHu&index=52&t=9s WilliamFiset Indexed Priority Queue
"""
import sys
sys.path.append('..\\..\\Stacks and Queues')

from queue import PriorityQueue
from math import inf
from indexed_priority_queue_pydict import minpq
from directed_graph import AdjacencyListGraph

"""
################################ GRAPH DATA STRUCTURE ################################
g a weighted graph that is implemented as an adjacency list
For each key in the graph there are a list of edge objects with
keys: cost and to

########################## LAZY DIJKSTRA'S ALGORITHM ##################################
g - adjacency list of weighted graph
n - the number of nodes in the graph
s - index of starting node (0 <= s < n)
e - index of end node (0 <= e < n)

This algorithm always selects the next most promising key-value pair from the PQ

This algorithm is lazy because we lazily delete outdated
key, value pairs in the priority queue.

We may have duplicate vertex indices in the priority queue (PQ)
But inserting a new key-value pair in O(logN) is much faster
then searching for the key in the PQ which takes O(N).
In PQs the elements are sorted by values not keys.

We make use of a visited array, vis, to track the visited node index
ie. so we don't revisit node indices. We also initialize a dist array
with all entries set to math.inf until we find a more optimum solution
Dijkstra's algorithm is a greedy algorithm becuase it queries the priority queue
for the local optimum solution

This algorithm can be greatly improved by using:
an indexed priority queue, a D-ary heap or a fibonacci heap
"""


def lazy_dijkstra_short_path_value(g, n, s, e):
    """
    Finds the value of the shortest path from the start node d
    to the end node e given a adjacency list graph
    """
    vis = [0] * n
    prev = [None] * n
    dist = [inf] * n
    dist[0] = 0
    pq = PriorityQueue()
    # note that priority queue sorts by the first value of a tuple by default
    pq.put((0, s))

    while pq.qsize() != 0:
        minValue, index = pq.get()
        vis[index] = 1
        # Optimization to ignore stale (dist, index) pairs
        if dist[index] < minValue:
            continue
        for edge in g[index]:
            # if we have visited that vertex then don't relax the edge
            if vis[edge.to]:
                continue
            newDist = dist[index] + edge.cost
            # update if we find a better solution
            if newDist < dist[edge.to]:
                prev[edge.to] = index
                dist[edge.to] = newDist
                pq.put((newDist, edge.to))
        # Significant optimization given that Dijsktra's algorithm is
        # a greedy algorithm. The value will not change as we visit future nodes.
        if index == e:
            return dist[e]
    return inf


def lazy_dijkstra(g, n, s):
    """
    Given a weighted directed graph g and a start node s return the distance to each node
    and the previous node visited before reaching the queried node on the optimal path.
    """
    vis = [0] * n
    prev = [None] * n
    dist = [inf] * n
    dist[0] = 0

    pq = PriorityQueue()
    # 2nd entry in tuple is the node index
    pq.put((0, s))

    while pq.qsize() != 0:
        minValue, index = pq.get()
        vis[index] = 1
        # Optimization to ignore stale (dist, index) pairs
        if dist[index] < minValue:
            continue
        for edge in g[index]:
            # if we have visited that vertex then don't relax the edge
            if vis[edge.to]:
                continue
            newDist = dist[index] + edge.cost
            # update if we find a better solution
            if newDist < dist[edge.to]:
                prev[edge.to] = index
                dist[edge.to] = newDist
                pq.put((newDist, edge.to))
    return (dist, prev)


def find_shortest_path(g, n, s, e):
    """
    Given a weighted directed graph g, a starting node s and an end node e return the shortest path.
    """
    dist, prev = lazy_dijkstra(g, n, s)
    path = []
    if (dist[e] == inf):
        return path
    # loop backwards from the end vertex
    path.append(e)
    i = e
    # prev[i] == None corresponds to the start node
    while prev[i] != None:
        path.append(prev[i])
        i = prev[i]
    return list(reversed(path))


"""
########################## EAGER DIJKSTRA'S ALGORITHM ##################################
# USEFUL DATA STRUCTURES
############### IndexedMinPQ ###############
In the PQ used in the lazy algorithm it's more efficient to insert a new
key-value pair in O(logN) then it is to update an existing key's value

This is inefficient for dense graphs because we end up with several stale
outdated key-value pairs in our PQ. The eager version avoids duplicate key-value
pairs by O(logN) updates using an Indexed Priority Queue (IPQ)

Resource: https://pypi.org/project/pqdict/0.1/

############### Optimal D-ary Heap ###############
A D-ary heap is a heap variant in which each node has D children.
The state of the art methods use D-ary heaps which reduce the cost of
decreaseKey operations by increasing the cost of removal operations.
Removal operations are much less common in dense graphs.

The best degree, D, to use is D = E/V which balances the cost of removal against
decreaseKey operations, improving the time complexity to:
T = O(E*log_{E/V}(V))

############### Fibonacci Heap ###################
The current state of the art method uses a Fibonacci heap which gives Dijkstra's algorithm
a time complexity of:
T = O(E + VlogV)

However, it should be noted that Fibonacci heaps are notoriously difficult to implement and
have a large enough constant amortized overhead to make them impractical unless your
graph is quite large.
"""
############## IMPLEMENTATION OF IPQ EAGER DIJKSTRA ####################


def eager_dijkstra(g, n, s):
    vis = [0] * n
    dist = [inf] * n
    prev = [None] * n
    dist[s] = 0
    ipq = minpq()
    # API expects two inputs
    # key and value
    ipq.additem(s, 0)

    while len(ipq) != 0:
        index, minValue = ipq.popitem()
        vis[index] = 1
        if dist[index] < minValue:
            continue
        for edge in g[index]:
            if vis[edge.to]:
                continue
            newDist = dist[index] + edge.cost
            if newDist < dist[edge.to]:
                dist[edge.to] = newDist
                prev[edge.to] = index
                if edge.to not in ipq:
                    ipq.additem(edge.to, newDist)
                else:
                    ipq.updateitem(edge.to, newDist)
    return (dist, prev)


###################################### TESTS ##########################################
# this example will enter the stale node optimization check
g1 = AdjacencyListGraph()
g1.add_edge(0, 1, 4)
g1.add_edge(0, 2, 1)
g1.add_edge(2, 3, 5)
g1.add_edge(1, 3, 1)
g1.add_edge(3, 4, 3)
g1.add_edge(2, 1, 2)

# this is a larger example
g2 = AdjacencyListGraph()
g2.add_edge(0, 1, 5)
g2.add_edge(1, 5, 3)
g2.add_edge(6, 5, 2)
g2.add_edge(1, 4, 1)
g2.add_edge(5, 4, 3)
g2.add_edge(1, 6, 2)
g2.add_edge(6, 4, 7)
g2.add_edge(4, 3, 8)
g2.add_edge(3, 2, 3)
g2.add_edge(6, 1, 3)
g2.add_edge(5, 0, 4)

print('Lazy Implementation with Priority Queue')
print('*' * 60)
print('Path to the shortest node :', find_shortest_path(g2, len(g2), 0, 2))
print()
print('Eager Implementation with an Indexed Priority Queue')
print('*' * 60)
dist, prev = eager_dijkstra(g1, len(g1), 0)
print('Distance to node indexes :', dist)
