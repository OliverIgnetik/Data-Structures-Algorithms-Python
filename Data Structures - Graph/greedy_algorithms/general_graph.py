class GraphEdge:
    def __init__(self, f, t, cost):
        self.cost = cost
        self.f = f
        self.t = t

    # edges sort by cost
    def __lt__(self, other):
        if self.cost < other.cost:
            return 1
        else:
            return 0

    def __le__(self, other):
        if self.cost <= other.cost:
            return 1
        else:
            return 0

    def __repr__(self):
        result = f'(from = {self.f}, to = {self.t}, cost = {self.cost})'
        return result


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

        ne = GraphEdge(f, t, cost)
        self.vertices[f].append(ne)
        self.num_edges += 1
        return


def make_complicated_graph1():
    g = AdjacencyListGraph()

    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 1)
    g.add_edge(0, 3, 4)

    g.add_edge(1, 0, 10)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 4, 0)

    g.add_edge(4, 1, 0)
    g.add_edge(4, 5, 1)
    g.add_edge(4, 7, 8)

    g.add_edge(7, 4, 8)
    g.add_edge(7, 5, 9)
    g.add_edge(7, 6, 12)

    g.add_edge(6, 7, 12)
    g.add_edge(6, 5, 6)
    g.add_edge(6, 3, 7)

    g.add_edge(3, 6, 7)
    g.add_edge(3, 2, 2)
    g.add_edge(3, 0, 4)
    g.add_edge(3, 5, 2)

    g.add_edge(2, 3, 2)
    g.add_edge(2, 5, 8)
    g.add_edge(2, 1, 3)
    g.add_edge(2, 0, 1)

    g.add_edge(5, 4, 1)
    g.add_edge(5, 3, 2)
    g.add_edge(5, 7, 9)
    g.add_edge(5, 6, 6)
    g.add_edge(5, 2, 8)

    return g


def make_complicated_graph2():
    g = AdjacencyListGraph()

    g.add_edge(0, 2, 0)
    g.add_edge(0, 5, 7)
    g.add_edge(0, 3, 5)
    g.add_edge(0, 1, 9)

    g.add_edge(1, 0, 9)
    g.add_edge(1, 3, -2)
    g.add_edge(1, 6, 4)
    g.add_edge(1, 4, 3)

    g.add_edge(4, 1, 3)
    g.add_edge(4, 6, 6)

    g.add_edge(6, 4, 6)
    g.add_edge(6, 1, 4)
    g.add_edge(6, 3, 3)
    g.add_edge(6, 5, 1)

    g.add_edge(3, 0, 5)
    g.add_edge(3, 1, -2)
    g.add_edge(3, 6, 3)
    g.add_edge(3, 5, 2)

    g.add_edge(2, 0, 0)
    g.add_edge(2, 5, 6)

    g.add_edge(5, 2, 6)
    g.add_edge(5, 0, 7)
    g.add_edge(5, 3, 2)
    g.add_edge(5, 6, 1)

    return g
