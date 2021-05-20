from math import inf
from typing import NamedTuple

################### DATA STRUCTURES ##############################
# Resources
# https://www.youtube.com/watch?v=pSqmAO-m7Lk   WilliamFiset Dijkstra's algorithm

############### Optimal D-ary Heap ###############
# A D-ary heap is a heap variant in which each node has D children.
# The state of the art methods use D-ary heaps which reduce the cost of
# decreaseKey operations by increasing the cost of removal operations. Removal operations
# are much less common in dense graphs.

# The best degree, D, to use is D = E/V to balance removals against decreaseKey operations
# improving the time complexity to :
# O(E*log_{E/V}(V))


# CREDIT
# https: // github.com/williamfiset/Algorithms/blob/master/src/main/java/com/williamfiset/algorithms/graphtheory/DijkstrasShortestPathAdjacencyListWithDHeap.java
class minIndexedDHeap:

    def __init__(self, degree: int, maxSize: int):
        self.D = max(2, degree)
        self.N = max(self.D + 1, maxSize)
        self.size = 0

        self.im = [0] * self.N
        self.pm = [0] * self.N
        self.child = [0] * self.N
        self.parent = [0] * self.N
        self.values = [0] * self.N

        for i in range(self.N):
            self.parent[i] = (i - 1) // self.D
            self.child[i] = i * self.D + 1
            self.pm[i] = self.im[i] = -1

    def __contains__(self, ki: int):
        return self.pm[ki] != -1

    def peekMinKeyIndex(self):
        return self.im[0]

    def pollMinKeyIndex(self):
        minki = self.peekMinKeyIndex()
        self.delete(minki)
        return minki

    def peekMinValue(self):
        return self.values[self.im[0]]

    def pollMinValue(self):
        minValue = self.peekMinValue()
        self.delete(self.peekMinKeyIndex())
        return minValue

    def insert(self, ki: int, value):
        if ki in self:
            raise KeyError('Index already exists')
        self.pm[ki] = self.size
        self.im[self.size] = ki
        self.values[ki] = value
        self.size += 1
        self.__swim(self.size)

    def delete(self, ki: int):
        i = self.pm[ki]
        self.size -= 1
        self.__swap(i, self.size)
        self.__sink(i)
        self.__swim(i)
        value = self.values[ki]
        self.values[ki] = None
        self.pm[ki] = -1
        self.im[self.size] = -1
        return value

    def update(self, ki: int, value):
        i = self.pm[ki]
        oldValue = self.values[ki]
        self.values[ki] = value
        self.__sink(i)
        self.__swim(i)
        return oldValue

    def decrease(self, ki: int, value):
        if (self.__less(value, self.values[ki])):
            self.values[ki] = value
            self.__swim(self.pm[ki])

    def increase(self, ki: int, value):
        if (self.__less(self.values[ki], value)):
            self.values[ki] = value
            self.__sink(self.pm[ki])

    # helper methods
    def __swim(self, i: int):
        while (self.__less(i, self.parent[i])):
            self.__swap(i, self.parent[i])
            i = parent[i]

    def __sink(self, i: int):
        j = self.__minchild(i)
        while j != -1:
            self.__swap(i, j)
            i = j
            j = self.__minchild(i)

    def __minchild(self, i: int):
        index = -1
        from_ = self.child[i]
        to = min(self.size, from_ + self.D)

        j = from_
        while j < to:
            if (self.__less(j, i)):
                index = i = j
            j += 1
        return index

    def __swap(self, i: int, j: int):
        self.pm[self.im[j]] = i
        self.pm[self.im[i]] = j
        tmp = self.im[i]
        self.im[i] = self.im[j]
        self.im[j] = tmp

    @staticmethod
    def __less(x, y):
        return x < y


# NamedTuple for Graph edge as we do not need to write new values to edges
class GraphEdge(NamedTuple):
    cost: int
    to: int


# Adjacency list implementation
class AdjacencyListGraph:

    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0
        self.num_edges = 0

    def __len__(self):
        return self.num_vertices

    def __contains__(self, n):
        return n in self.vertices

    def __getitem__(self, key):
        return self.vertices[key]

    def add_vertex(self, key):
        if key not in self.vertices:
            raise KeyError('Vertex already exists in the graph')
        else:
            self.vertices[key] = list()
            self.num_vertices += 1

    def add_edge(self, f, t, cost):
        if f not in self.vertices:
            self.vertices[f] = list()
            self.num_vertices += 1
        if t not in self.vertices:
            self.vertices[t] = list()
            self.num_vertices += 1

        ne = GraphEdge(cost, t)
        self.vertices[f].append(ne)
        self.num_edges += 1
        return


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
