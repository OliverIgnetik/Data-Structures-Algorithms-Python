""""
################################ Prim's Algorithm ################################

Resources
- https://www.youtube.com/watch?v=MaaSoZUEoos Joe James
- https://www.youtube.com/watch?v=K_1urzWrzLs BacktoBackSWE
- https://www.youtube.com/watch?v=jsmMtJpPnhU&list=PLDV1Zeh2NRsDGO4--qE8yH72HFL1Km93P&index=30 WilliamFiset
- https://www.programiz.com/dsa/prim-algorithm Programiz

Prim's algorithm finds the minimum spanning tree (MST) of a weighted graph
Minimum Spanning Tree subset of edges that:

1. Reaches every vertex
2. Has no minimum total weight
3. Has no cycles

Prim's algorithm does this by building a tree from a single
vertex by adding the cheapest edge to an unmapped vertex. In
other words it works on local optimization.

We can make use of a tree perimeter to select the best edge
out of the tree.

########################## TIME COMPLEXITY ##########################
 T = O(ElogE)

NOTE: this is a lazy implementation of prim's algorithm

########################## APPLICATIONS ##########################

1. Laying cables of electrical wiring
2. In network design
3. To make protocols in network cycles

"""

########################## IMPLEMENTATION ##########################
INF = 9999999
# number of vertices in graph
V = 5
# create a 2d array of size 5x5
# for adjacency matrix to represent graph

# the entries are encoded as follows:
# the G[i][j] is the edge weight from the ith
# vertex index to the jth vertex index

# NOTE: the diagonal entries are all zero
G = [[0, 9, 75, 0, 0],
     [9, 0, 95, 19, 42],
     [75, 95, 0, 51, 66],
     [0, 19, 51, 0, 31],
     [0, 42, 66, 31, 0]]
# create a array to track selected vertex
# selected will become true otherwise false
selected = [0, 0, 0, 0, 0]
# set number of edge to 0
no_edge = 0
# the number of egde in minimum spanning tree will be
# always less than(V - 1), where V is number of vertices in
# graph
# choose 0th vertex and make it true
selected[0] = True
# print for edge and weight
print("Edge : Weight\n")
while (no_edge < V - 1):
    # For every vertex in the set S, find the all adjacent vertices
    # , calculate the distance from the vertex selected at step 1.
    # if the vertex is already in the set S, discard it otherwise
    # choose another vertex nearest to selected vertex  at step 1.
    minimum = INF
    x = 0
    y = 0
    for i in range(V):
        # only scan the edges of selected nodes
        if selected[i]:
            for j in range(V):
                # not in selected and there is an edge
                if ((not selected[j]) and G[i][j]):
                    # update minimum if we find more optimal edge that
                    # is connected to the selected nodes
                    if minimum > G[i][j]:
                        minimum = G[i][j]
                        x = i
                        y = j
    print(str(x) + "-" + str(y) + ":" + str(G[x][y]))
    # set the next most promising node to True
    selected[y] = True
    no_edge += 1
