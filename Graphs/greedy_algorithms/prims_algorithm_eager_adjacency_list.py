import sys
sys.path.append('../../Stacks and Queues')

from math import inf
from general_graph import make_complicated_graph2
from indexed_priority_queue_pydict import minpq

"""
###################################### OVERVIEW #####################################

Given an undirected graph with weighted edges, a Minimum Spanning
Tree (MST) is a subset of the edges in the graph which connects all the
vertices together (without creating cycles) while minimizing the total edge cost

Prim's algorithm finds the MST on an undirected graph

###################################### DATA STRUCTURES ######################################
################ EDGE OBJECTS ################
It makes use of a minimum priority queue that sorts edges based on minimum edge cost
Although the graphs we will analyse will be undirected the edges will be represented
by two directed edges.
Each edge is of the form {start_node, end_node , cost}

################ GRAPH ################
Undirected Adjacency list representation of a graph. Undirected edges are represented by two
directed edges.

NamedTuple is appropriate if we don't want need to change the __lt__ dunder method

################ PRIORITY QUEUE ################
We need to make use of minimum priority queue to track the local optimum edge choice. 
NOTE: that by making use of an indexed priority queue/ D-ary heap we can improve the performance 
on dense graphs due to the reduced cost of update vs delete operations. 

NOTE: By using an IPQ we will avoid stale edges. 

###################################### TIME COMPLEXITY ######################################
Through the use of an Indexed Priority Queue the time complexity is:
T = O(ElogV)
"""

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
