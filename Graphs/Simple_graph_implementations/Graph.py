from Vertex import Vertex
from collections import deque
# Adjacency List implementation of an directed graph (digraph)


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

    """
    DFS OVERVIEW 
    ----
    DFS - goes deep, exhaustive path finding
    Plunges depth first into a graph without regard for which edge 
    it takes next until it cannot go any further at which point it
    and continues

    NOTE: PRIMARY DATA STRUCTURE LIFO (STACK)

    Applications 
    ----
    1. Placing reachable components into groups by starting DFS at every node
    2. Compute a graph's MST
    3. Detect and find cycles in a graph
    4. Check if a graph is bipartite
    4. Find strongly connected components 
    5. Topologically sort the nodes of a graph
    6. Find bridges and articulation points
    7. Find augmenting paths in a flow network 
    8. Generate mazes
    """

    def dfs(self, vert_id, target_id):
        """
        Complexity 
        ----
        Time : O(|V| + |E|)
        """
        s = list()
        # take a set of words not chars
        visited = set(vert_id.split(' '))
        print(vert_id)
        # append all neighbours
        for n in self.vertList[vert_id].connectedTo.keys():
            s.append(n.id)

        while len(s) > 0:
            u = s.pop()
            node_u = self.vertList[u]
            # if we haven't visited this node then process it's neighbours
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
        # If we traverse all the nodes in the graph then the path doesn't exist
        return False

    """
    BFS OVERVIEW
    ----
    It is particularly useful for one thing : finding the shortest path on unweighted graphs. 

    BFS starts at some arbitrary node of a graph and explores the neighbour nodes first, 
    before moving to the next level neighbours

    NOTE: PRIMARY DATA STRUCTURE FIFO (QUEUE)
    """

    def bfs(self, vert_id, target_id):
        """
        Complexity 
        ----
        Time : O(|V| + |E|)
        """
        q = deque()
        # take a set of words not chars
        visited = set(vert_id.split(' '))
        print(vert_id)
        # append all neighbours
        for n in self.vertList[vert_id].connectedTo.keys():
            q.append(n.id)

        while len(q) > 0:
            u = q.popleft()
            node_u = self.vertList[u]
            # if we haven't visited this node then process it's neighbours
            if node_u.id not in visited:
                visited.add(node_u.id)
                print(node_u.id)
                if node_u.id == target_id:
                    print(f'Path between {vert_id} and {node_u.id} exists')
                    return True
                for n in node_u.connectedTo.keys():
                    node_v = self.vertList[n.id]
                    if node_v.id not in visited:
                        q.append(node_v.id)
        # If we traverse all the nodes in the graph then the path doesn't exist
        return False

    def findComponentGroupings(self):
        """
        Init a visited structure to keep track of nodes visited
        Init a count variable for grouping nodes
        Init a structure to keep track of which group each node belongs to
        Iterate through each node and perform DFS and increment the count each time we exit DFS
        """
        pass
