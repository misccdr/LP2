def bfs_recursion(graph, start, visited = None, queue = None):
    if visited is None:
        visited = set()

    if queue is None:
        queue = []

    visited.add(start)
    print(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)

    if queue:
        next_vertex = queue.pop(0)
        bfs_recursion(graph, next_vertex, visited, queue)

graph = {
    '1': ['5', '4', '2'],
    '5': ['1'],
    '4': ['1'],
    '2': ['1', '7', '6', '3'],
    '7': ['2'],
    '6': ['2'],
    '3':['2']
}

bfs_recursion(graph, '1')