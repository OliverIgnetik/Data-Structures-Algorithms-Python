# Resources
# https://www.youtube.com/watch?v=pSqmAO-m7Lk   WilliamFiset
# https://www.youtube.com/watch?v=pVfj6mxhdMw Computer Science
# https://www.youtube.com/watch?v=K_1urzWrzLs BacktoBackSWE
# https://www.programiz.com/dsa/dijkstra-algorithm  Programiz
# https://www.youtube.com/watch?v=U9Raj6rAqqs&list=PLj8W7XIvO93oxLOZTi8JFghuRcKieIZU-&index=3 Joe James


# Dijkstra's Algorithm in Python

# OVERVIEW
# It is a greedy algorithm because it selects the locally optimum solution

# ASSUMPTION
# The main assumptions of Dijkstra's algorithm is that the graphs
# have non-negative edge weights

# Use of min priority queue or min heap to find the next nearest vertex
# Known as a greedy algorithm
# Time complexity O(ElogV)


import sys

# Providing the graph
vertices = [[0, 0, 1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 1, 0],
            [1, 1, 0, 1, 1, 0, 0],
            [1, 0, 1, 0, 0, 0, 1],
            [0, 0, 1, 0, 0, 1, 0],
            [0, 1, 0, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 1, 0]]

edges = [[0, 0, 1, 2, 0, 0, 0],
         [0, 0, 2, 0, 0, 3, 0],
         [1, 2, 0, 1, 3, 0, 0],
         [2, 0, 1, 0, 0, 0, 1],
         [0, 0, 3, 0, 0, 2, 0],
         [0, 3, 0, 0, 2, 0, 1],
         [0, 0, 0, 1, 0, 1, 0]]

# Find which vertex is to be visited next


def to_be_visited():
    global visited_and_distance
    v = -10
    for index in range(num_of_vertices):
        if visited_and_distance[index][0] == 0 \
            and (v < 0 or visited_and_distance[index][1] <=
                 visited_and_distance[v][1]):
            v = index
    return v


num_of_vertices = len(vertices[0])

visited_and_distance = [[0, 0]]
for i in range(num_of_vertices-1):
    visited_and_distance.append([0, sys.maxsize])

for vertex in range(num_of_vertices):

    # Find next vertex to be visited
    to_visit = to_be_visited()
    for neighbor_index in range(num_of_vertices):

        # Updating new distances
        if vertices[to_visit][neighbor_index] == 1 and \
                visited_and_distance[neighbor_index][0] == 0:
            new_distance = visited_and_distance[to_visit][1] \
                + edges[to_visit][neighbor_index]
            if visited_and_distance[neighbor_index][1] > new_distance:
                visited_and_distance[neighbor_index][1] = new_distance

        visited_and_distance[to_visit][0] = 1

i = 0

# Printing the distance
for distance in visited_and_distance:
    print("Distance of ", chr(ord('a') + i),
          " from source vertex: ", distance[1])
    i = i + 1
