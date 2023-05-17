import sys
import collections

input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
shark = []

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
    for j in range(m):
        if row[j] == 1:
            shark.append((i, j))

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, -1, 1]

ans = 0
def calcDistance(shark):
    sx, sy = shark
    q = collections.deque([(sx, sy)])
    visited = [[-1] * m for _ in range(n)]
    visited[sx][sy] = 0
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = dx[d] + x
            ny = dy[d] + y
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                if graph[nx][ny] == 1:
                    return visited[x][y]
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
        for d in range(4, 8):
            nx = dx[d] + x
            ny = dy[d] + y
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1 and graph[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

    return max([max(i) for i in visited])

for s in shark:
    ans = max(ans, calcDistance(s))

print(ans)

