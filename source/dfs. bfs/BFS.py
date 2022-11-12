from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[v]:
                queue.append(i)
                visited[i] = True