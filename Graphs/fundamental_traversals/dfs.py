"""
Basic DFS implementation 

Recursive and stack based approaches

References 
- https://www.youtube.com/watch?v=PMMc4VsIacU Reducible
- https://www.youtube.com/watch?v=TIbUeeksXcI&t=535s BackToBackSWE
"""


def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            # add the unvisited adjacent vertices
            stack.extend(sorted(graph[vertex] - visited, reverse=True))
    return visited


def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    if start not in visited:
        print(start)
        visited.add(start)
    for nxt in graph[start] - visited:
        dfs_recursive(graph, nxt, visited)
    return visited


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        print(vertex)
        for nxt in graph[vertex] - set(path):
            if nxt == goal:
                yield path + [nxt]
            else:
                stack.append((nxt, path + [nxt]))


# adjacency list
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

print('DFS')
print(dfs(graph, 'F'))
print('DFS recursive')
print(dfs_recursive(graph, 'F'))
print('DFS PATHS')
print(list(dfs_paths(graph, 'F', 'A')))
