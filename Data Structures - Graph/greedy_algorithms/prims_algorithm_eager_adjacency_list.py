import sys
sys.path.append('../../Data Structures - Stacks and Queues')

from math import inf
from general_graph import make_complicated_graph2
from indexed_priority_queue_pydict import minpq

###################################### OVERVIEW #####################################

# Given an undirected graph with weighted edges, a Minimum Spanning
# Tree (MST) is a subset of the edges in the graph which connects all the
# vertices together (without creating cycles) while minimizing the total edge cost

# Prim's is a greedy algorithm that work's well on dense graphs. On these
# graphs, Prim's meets or improves on the time bounds of its rivals (Kruskal's and Boruvka's)

###################################### DATA STRUCTURES ######################################
################ EDGE OBJECTS ################
# It makes use of a minimum priority queue that sorts edges based on minimum edge cost
# Although the graphs we will analyse will be undirected the edges will be represented
# by two directed edges.
# Each edge is of the form {start_node, end_node , cost}

# this will work with python's PriorityQueue becuase it sorts on the first item

################ GRAPH ################
# Undirected Adjacency list representation of a graph. Undirected edges are represented by two
# directed edges.

# NamedTuple is appropriate if we don't want the edge data to change

################ PRIORITY QUEUE ################
# We need to make use of minimum priority queue to track the local optimum edge choice
# For the eager implementation we will use .
# Note that by making use of an indexed priority queue/ D-ary heap we can
# improve the performance on dense graphs due to the reduced cost of update vs delete operations.

# NOTE: Python's standard library PriorityQueue sorts on the first input a tuple by default

###################################### TIME COMPLEXITY ######################################
# Through the use of an Indexed Priority Queue the time complexity is:
# T = O(ElogV)


###################################### IMPLEMENTATION ######################################
def eager_prim(g, n, s=0):

    # helper function
    def relaxEdgesAtNode(currentNodeIndex):
        vis[currentNodeIndex] = 1
        edges = g[currentNodeIndex]

        for edge in edges:
            destNodeIndex = edge.t

            if vis[destNodeIndex]:
                continue

            if destNodeIndex not in ipq:
                ipq.additem(destNodeIndex, edge)

            else:
                if ipq[destNodeIndex].cost > edge.cost:
                    ipq.updateitem(destNodeIndex, edge)

    # intiliaze values
    vis = [0] * n
    m = n - 1
    edgeCount, mstCost = 0, 0
    mstEdges = []
    # inialize a priority queue with maxsize equal to the total number of edges
    ipq = minpq()

    relaxEdgesAtNode(s)

    while len(ipq) and edgeCount != m:
        (destNodeIndex, edge) = ipq.popitem()

        edgeCount += 1
        mstEdges.append(edge)
        mstCost += edge.cost

        relaxEdgesAtNode(destNodeIndex)

    if edgeCount != m:
        return (None, None)
    return (mstCost, mstEdges)


g = make_complicated_graph2()

cost, edges = eager_prim(g, len(g), 0)

print(f'Total cost is {cost}')
for edge in edges:
    print(edge)
