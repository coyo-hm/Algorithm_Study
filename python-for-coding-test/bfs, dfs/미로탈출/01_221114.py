from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(n)]

queue = deque([(0, 0)])    

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
  x, y = queue.popleft()
  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
      graph[nx][ny] = graph[x][y] + 1
      queue.append((nx, ny))

print(graph[n - 1][m - 1])