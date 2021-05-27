from queue import PriorityQueue
from math import inf
from general_graph import make_complicated_graph1

###################################### OVERVIEW #####################################

# Given an undirected graph with weighted edges, a Minimum Spanning
# Tree (MST) is a subset of the edges in the graph which connects all the
# vertices together (without creating cycles) while minimizing the total edge cost.

# Prim's is a greedy algorithm that work's well to finds MSTs on dense graphs. On denser
# graphs, Prim's meets or improves on the time bounds of its rivals (Kruskal's and Boruvka's).
# As each node is processed, all it's edges are relaxed and those that point to unvisited nodes,
# are added to the PQ. Whenever, the PQ is poll the edge with the lowest cost is selected.

###################################### DATA STRUCTURES ######################################
################ EDGE OBJECTS ################
# It makes use of a minimum priority queue that sorts edges based on minimum edge cost
# Although the graphs we will analyse will be undirected, the undirected edges will be represented
# by two directed edges. Each edge is of the form {start_node, end_node , cost}

################ GRAPH ################
# Undirected Adjacency list representation of a graph. Undirected edges are represented by two
# directed edges.

# NamedTuple is appropriate if we don't want the edge data to change

################ PRIORITY QUEUE ################
# We need to make use of minimum priority queue to track the local optimum edge choice
# For the lazy implementation we will just use the standard library priority queue.

# NOTE: that by making use of an indexed priority queue we can
# improve the performance on dense graphs due to the reduced cost of update vs delete operations.

# NOTE: Python's standard library PriorityQueue sorts on the first input a tuple by default
# However, we can set the dunder method for __lt__, __le__ so that the edge objects are compared by cost

###################################### TIME COMPLEXITY ######################################
# The lazy version of Prim's has a runtime of:
# T = O(ElogE)

# But the eager version has a better runtime with:
# T = O(ElogV)


###################################### IMPLEMENTATION ######################################
def lazy_prim(g, n, s=0):

    # helper function
    def add_edges(nodeIndex):
        vis[nodeIndex] = 1
        edges = g[nodeIndex]

        for edge in edges:
            if not vis[edge.t]:
                pq.put(edge)

    # intiliaze values
    vis = [0] * n
    m = n - 1
    edgeCount, mstCost = 0, 0
    mstEdges = []
    # inialize a priority queue with maxsize equal to the total number of edges
    pq = PriorityQueue(g.num_edges)

    add_edges(s)

    while not pq.empty() and edgeCount != m:
        edge = pq.get()
        nodeIndex = edge.t

        if vis[nodeIndex]:
            continue

        edgeCount += 1
        mstEdges.append(edge)
        mstCost += edge.cost

        add_edges(nodeIndex)

    if edgeCount != m:
        return (None, None)
    return (mstCost, mstEdges)


g = make_complicated_graph1()

cost, edges = lazy_prim(g, len(g), 0)

print(f'Total cost is {cost}')
for edge in edges:
    print(edge)
