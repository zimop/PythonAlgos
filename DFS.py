def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
       
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
            
adjacency_list = {1: [2, 5], 2: [1, 3], 3: [2, 4], 4: [5, 3], 5: [1, 4]}
dfs(adjacency_list, 1, None)