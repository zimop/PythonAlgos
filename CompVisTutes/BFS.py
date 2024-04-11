def bfs(graph, start):
    queue = []
    visited = []
    visited.append(start)
    queue.append(start)
    
    while queue:
        value = queue.pop(0)
        print(value)
        for neighbor in graph[value]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

adjacency_list = {1: [2, 5], 2: [1, 3], 3: [2, 4], 4: [5, 3], 5: [1, 4]}
bfs(adjacency_list, 1)