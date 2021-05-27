class Edge:

    def __init__(self, arg_src, arg_dst, arg_weight):
        self.src = arg_src
        self.dst = arg_dst
        self.weight = arg_weight


class Graph:

    def __init__(self, arg_num_nodes, arg_edgelist):
        self.num_nodes = arg_num_nodes
        self.edgelist = arg_edgelist
        self.parent = []
        self.rank = []
        # mst stores edges of the minimum spanning tree
        self.mst = []

    def FindParent(self, node):

        if self.parent[node] == node:
            return node
        return self.FindParent(self.parent[node])

    def KruskalMST(self):

        # Sort objects of an Edge class based on attribute (weight)
        self.edgelist.sort(key=lambda Edge: Edge.weight)

        self.parent = [None] * self.num_nodes
        self.rank = [None] * self.num_nodes

        for n in range(self.num_nodes):
            # Every node is the parent of itself at the beginning
            self.parent[n] = n
            self.rank[n] = 0   # Rank of every node is 0 at the beginning

        for edge in self.edgelist:
            root1 = self.FindParent(edge.src)
            root2 = self.FindParent(edge.dst)

            # Parents of the source and destination nodes are not in the same subset
            # Add the edge to the spanning tree
            if root1 != root2:
                self.mst.append(edge)
                if self.rank[root1] < self.rank[root2]:
                    self.parent[root1] = root2
                    self.rank[root2] += 1
                else:
                    self.parent[root2] = root1
                    self.rank[root1] += 1

        print("\nEdges of minimum spanning tree in graph :", end=' ')
        cost = 0
        for edge in self.mst:
            print("[" + str(edge.src) + "-" + str(edge.dst) +
                  "](" + str(edge.weight) + ")", end=' ')
            cost += edge.weight
        print("\nCost of minimum spanning tree : " + str(cost))


def main():

    # Edge(source, destination, weight)
    num_nodes = 6
    e1 = Edge(0, 1, 4)
    e2 = Edge(0, 2, 1)
    e3 = Edge(0, 3, 5)
    e4 = Edge(1, 3, 2)
    e5 = Edge(1, 4, 3)
    e6 = Edge(1, 5, 3)
    e7 = Edge(2, 3, 2)
    e8 = Edge(2, 4, 8)
    e9 = Edge(3, 4, 1)
    e10 = Edge(4, 5, 3)

    g1 = Graph(num_nodes, [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10])
    g1.KruskalMST()

    num_nodes = 7
    a = Edge(0, 1, 1)
    b = Edge(0, 2, 2)
    c = Edge(0, 3, 1)
    d = Edge(0, 4, 1)
    e = Edge(0, 5, 2)
    f = Edge(0, 6, 1)
    g = Edge(1, 2, 2)
    h = Edge(1, 6, 2)
    i = Edge(2, 3, 1)
    j = Edge(3, 4, 2)
    k = Edge(4, 5, 2)
    l = Edge(5, 6, 1)

    g2 = Graph(num_nodes, [a, b, c, d, e, f, g, h, i, j, k, l])
    g2.KruskalMST()


if __name__ == "__main__":
    main()
