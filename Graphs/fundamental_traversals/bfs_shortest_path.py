def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        # use of a queue in contrast to dfs which uses a stack
        vertex = queue.pop(0)
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited


def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        # Go through the neighbours you haven't visited
        for nv in graph[vertex] - set(path):
            if nv == goal:
                # yield is used in conjuction with the next keyword
                yield path + [nv]
            else:
                queue.append((nv, path + [nv]))


def shortest_path(graph, start, goal):
    try:
        # next will just take the next element from an iterator
        # this will correspond to the shortest path as it will enter the list first
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None


graph = {'A': set(['B', 'C', 'I']),
         'B': set(['A', 'D', 'E', 'G']),
         'C': set(['A', 'F']),
         'D': set(['B', 'J']),
         'E': set(['B', 'F', 'H']),
         'F': set(['C', 'E']),
         'G': set(['B']),
         'H': set(['E']),
         'I': set(['A']),
         'J': set(['D'])
         }

print('BFS TRAVERSAL')
print(bfs(graph, 'F'))

print('BFS PATHS')
print(list(bfs_paths(graph, 'F', 'J')))

print('SHORTEST PATH')
print(shortest_path(graph, 'F', 'J'))
