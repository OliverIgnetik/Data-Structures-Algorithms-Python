from typing import NamedTuple


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
