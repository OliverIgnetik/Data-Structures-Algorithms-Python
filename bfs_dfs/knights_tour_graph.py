# https: // bradfieldcs.com/algos/graphs/knights-tour/

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.__color = 'white'

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def setColor(self, color):
        self.__color = color

    def getColor(self):
        return self.__color

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


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

# use a adjacency list because otherwise the matrix will be about 8% full
# we use a DFS search tree for exhaustive path searching


def knightGraph(bdSize):
    ktGraph = Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            # id for current node of interest
            nodeId = posToNodeId(row, col, bdSize)
            newPositions = genLegalMoves(row, col, bdSize)
            for e in newPositions:
                # get the node id for the other position
                nid = posToNodeId(e[0], e[1], bdSize)
                ktGraph.addEdge(nodeId, nid)
    return ktGraph


def posToNodeId(row, column, board_size):
    return (row * board_size) + column


def nodeIdToPos(nodeId, board_size):
    return (nodeId//board_size, nodeId % board_size)


def genLegalMoves(x, y, bdSize):
    newMoves = []
    # generic movesets
    moveOffsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
                   (1, -2), (1, 2), (2, -1), (2, 1)]
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        # check if each of the new moves are legal positions on the board
        if legalCoord(newX, bdSize) and legalCoord(newY, bdSize):
            newMoves.append((newX, newY))
    return newMoves


def legalCoord(x, bdSize):
    if x >= 0 and x < bdSize:
        return True
    else:
        return False


def knightTour(n, path, u, limit):
    # setting color to gray indicates it has been visited
    u.setColor('gray')
    path.append(u)
    # keep going until the depth is the same as the limit
    if n < limit:

        nbrList = list(u.getConnections())
        i = 0
        done = False
        # go through all the neighbours until you find one that solves the problem
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == 'white':
                done = knightTour(n+1, path, nbrList[i], limit)
            i = i + 1
        # if you don't find any solutions backtrack
        # ie. this part of the search space returns false
        if not done:
            path.pop()
            u.setColor('white')
    else:
        # this code will only evaluate when the depth of the recursion is equal to the number of positions on the board
        done = True
    return done


dimensions = 5

ktGraph = knightGraph(dimensions)

limit = dimensions**2
start_point = ktGraph.vertList[0]
path = []
depth = 1

knights_tour = knightTour(depth, path, start_point, limit)
print('MOVE SEQUENCE')
print('-'*60)
for node in path:
    print(
        'node id : {:<10d} position : {:<20s}'.format(node.getId(), str(nodeIdToPos(node.getId(), dimensions))))
