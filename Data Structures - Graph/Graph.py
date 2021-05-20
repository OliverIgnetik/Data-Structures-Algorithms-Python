from Vertex import Vertex


# Adjacency List implementation of an undirected graph
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    def dfs(self, vert_id, target_id):
        s = list()
        # take a set of words not chars
        visited = set(vert_id.split(' '))
        print(vert_id)
        for n in self.vertList[vert_id].connectedTo.keys():
            s.append(n.id)

        while len(s) > 0:
            u = s.pop()
            node_u = self.vertList[u]
            # if we haven't visited it
            if node_u.id not in visited:
                visited.add(node_u.id)
                print(node_u.id)
                if node_u.id == target_id:
                    print(f'Path between {vert_id} and {node_u.id} exists')
                    return True
                for n in node_u.connectedTo.keys():
                    node_v = self.vertList[n.id]
                    if node_v.id not in visited:
                        s.append(node_v.id)

        return False
