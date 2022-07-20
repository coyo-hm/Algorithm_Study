import collections
N, M = map(int, input().split())
graph = []

for _ in range(N):
  graph.append(list(map(int, list(input()))))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
q = collections.deque([(0,0)])

while q:
  x, y = q.popleft()
  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    if(0 <= nx < N and 0 <= ny < M):
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        q.append((nx, ny))

print(graph[N - 1][M - 1])