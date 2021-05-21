######################## Kruskal's algorithm ########################
# Given an undirected graph with weighted edges, a Minimum Spanning
# Tree (MST) is a subset of the edges in the graph which connects all the
# vertices together (without creating cycles) while minimizing the total edge cost

# TIME COMPLEXITY
# T = O(ElogV)

# RESOURCES
# https://www.youtube.com/watch?v=JZBQLXgSGfs William Fiset Kruskal's algorithm
# https://www.youtube.com/watch?v=0jNmHPfA_yE Union find operation
# https://www.youtube.com/watch?v=qOv8K-AJ7o0&t=35s Back To Back SWE Kruskal's algorithm
# https://www.hackerearth.com/practice/algorithms/graphs/minimum-spanning-tree/tutorial/ hackerearth MST

############ IMPLEMENTATION ############

# 1. Sort edges by ascending edge weight

# 2. Walk through the sorted edges and look at the two nodes the edge belongs to, if the
# nodes are already unified we don't include this edge, otherwise we include it and unify the nodes
# NOTE: it is crucial you don exclude the edge which joins nodes that are already unified or you will create a cycle
# which is not allowed in a MST

# 3. The algorithm terminates when every edge has been processed or all the vertices have been unified.

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # Search function

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    #  Applying Kruskal algorithm
    def kruskal_algo(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        for u, v, weight in result:
            print("%d - %d: %d" % (u, v, weight))


g = Graph(6)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 2)
g.add_edge(1, 0, 4)
g.add_edge(2, 0, 4)
g.add_edge(2, 1, 2)
g.add_edge(2, 3, 3)
g.add_edge(2, 5, 2)
g.add_edge(2, 4, 4)
g.add_edge(3, 2, 3)
g.add_edge(3, 4, 3)
g.add_edge(4, 2, 4)
g.add_edge(4, 3, 3)
g.add_edge(5, 2, 2)
g.add_edge(5, 4, 3)
g.kruskal_algo()
