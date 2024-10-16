"""
##########################################################
Overview 
Trace the path that a knight makes on an NxN chessboard to visit every square
Conditions
The knight must only visit each square once

##########################################################
Runtime Complexity
##########################################################
NOTE: the search space tree is related to time complexity 
NOTE: the graph size is related to space complexity

##########################################################
Time 
O(k^N)
k = average branching factor
NOTE: Key tree theory 
Nodes in a binary tree of height N = 2^N - 1  
Nodes in a general tree of height N = k^N - 1

- For a board that is 5x5 the search space tree will be 25 levels deep (counting the first level as 1). 
  k = 3.8 and there are : 
    3.8^25-1 = 3.12 x 10^14 nodes
- For an 8x8 board the search space tree will be 64 levels deep
  k = 5.25 and there are : 
    1.3x10^46 nodes

Remember that there are multiple solutions to the problem so we don't have to explore every node. 

##########################################################
Space
O(N^2)
There are NxN nodes in the graph

##########################################################
Resources
- https://bradfieldcs.com/algos/graphs/knights-tour/ implementation hints
- https://runestone.academy/runestone/books/published/pythonds/Graphs/KnightsTourAnalysis.html time complexity 
"""


from typing import List, Tuple


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.setColor('white')

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
            # explict return None statement
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
Use an adjacency list because otherwise the matrix will be about 8% full
we use a DFS search tree for exhaustive path searching
"""


def knightGraph(bdSize: int) -> Graph:
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


def posToNodeId(row: int, column: int, board_size: int) -> int:
    return (row * board_size) + column


def nodeIdToPos(nodeId: int, board_size: int) -> Tuple[int, int]:
    return (nodeId // board_size, nodeId % board_size)


def genLegalMoves(x: int, y: int, bdSize: int) -> List[Tuple[int, int]]:
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


def legalCoord(x: int, bdSize: int) -> bool:
    if x >= 0 and x < bdSize:
        return True
    else:
        return False


def knightTour(depth: int, path: List[Vertex], currentVertex: Vertex, limit: int) -> bool:
    # setting color to gray indicates it has been visited
    currentVertex.setColor('gray')
    path.append(currentVertex)
    # keep going until the depth is the same as the limit
    if depth < limit:

        nbrList = list(currentVertex.getConnections())
        i = 0
        done = False
        # go through all the neighbours until you find one that solves the problem
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == 'white':
                done = knightTour(depth + 1, path, nbrList[i], limit)
            i = i + 1
        # if you don't find any solutions backtrack
        # ie. this part of the search space returns false
        if not done:
            path.pop()
            currentVertex.setColor('white')
    else:
        # this code will only evaluate when the depth of the recursion is equal to the number of positions on the board
        done = True
    return done


dimensions = 5

ktGraph = knightGraph(dimensions)

limit = dimensions**2
start_point = ktGraph.vertList[4]
path = []
depth = 1

knights_tour = knightTour(depth, path, start_point, limit)
print('MOVE SEQUENCE')
print('-' * 60)
for node in path:
    print(
        'node id : {:<10d} position : {:<20s}'.format(node.getId(), str(nodeIdToPos(node.getId(), dimensions))))
