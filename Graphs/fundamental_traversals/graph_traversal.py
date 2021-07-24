"""
Traversals OOP approach 

BFS and DFS explanation
- https://www.youtube.com/watch?v=TIbUeeksXcI&t=532s

REFERENCE FOR CODE
- https://www.youtube.com/watch?v=-uR7BSfNJko&t=421s

Graph Fundamentals
In degree 
The number of incident edges that point to the vertex 

Out degree 
The number of incident edges that leave the vertex

Connectivity
In a digraph it is not always possible for a pair of nodes 
to be reachable from one another
Connectiveness - Only one node is reachable from the other
Strongly connected - Both nodes are reachable from one another

Strongly connected component - maximal subgraph that is strongly connected (ie. every node is reachable from every other node)
"""


class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = list()

        self.distance = 9999
        self.color = 'black'

    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()


class Graph:
    vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
                if key == v:
                    value.add_neighbor(u)
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(
                'Vertex : {:<3s} Neighbours : {:<25s} Level : {:<3s}'.format(key, str(self.vertices[key].neighbors), str(self.vertices[key].distance)))

    def bfs(self, vert):
        q = list()
        vert.distance = 0
        vert.color = 'red'
        print(vert.name)
        for v in vert.neighbors:
            self.vertices[v].distance = vert.distance + 1
            q.append(v)

        while len(q) > 0:
            u = q.pop(0)
            node_u = self.vertices[u]
            # This condition is needed to avoid processing the same node more then once
            # There will be stale nodes that we have already visited on the queue
            if node_u.color == 'black':
                node_u.color = 'red'
                print(node_u.name)
                for v in node_u.neighbors:
                    node_v = self.vertices[v]
                    if node_v.color == 'black':
                        q.append(v)
                        # this line is used in conjuction with the node_u.color == 'black'
                        # use case : non-uniformily weighted graph
                        if node_v.distance > node_u.distance + 1:
                            node_v.distance = node_u.distance + 1

    def dfs(self, vert, target):
        s = list()
        vert.color = 'red'
        print(vert.name)
        for v in vert.neighbors:
            s.append(v)

        while len(s) > 0:
            u = s.pop()
            node_u = self.vertices[u]
            # if we haven't visited it
            if node_u.color == 'black':
                node_u.color = 'red'
                print(node_u.name)
                if node_u.name == target:
                    print(f'Path between {vert.name} and {node_u.name} exists')
                    return True
                for v in node_u.neighbors:
                    node_v = self.vertices[v]
                    if node_v.color == 'black':
                        s.append(v)


g = Graph()
g.add_vertex(Vertex('A'))
g.add_vertex(Vertex('B'))

for i in range(ord('A'), ord('K')):
    g.add_vertex(Vertex(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH',
         'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
    g.add_edge(edge[:1], edge[1:])

print('BFS Traversal')
print('-' * 60)
g.bfs(g.vertices['C'])
print()

print('GRAPH AFTER BFS')
print('-' * 60)
g.print_graph()
print()

for vertex in g.vertices.values():
    vertex.color = 'black'
    vertex.distance = 9999

# look for a path between C and E
print('DFS Traversal up to target')
print('-' * 60)
g.dfs(g.vertices['C'], 'E')
