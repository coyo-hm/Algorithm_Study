import sys
import collections

input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
shark = collections.deque([])

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
    for j in range(m):
        if row[j] == 1:
            shark.append((i, j))

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, -1, 1]


while shark:
    x, y = shark.popleft()
    for d in range(8):
        nx = dx[d] + x
        ny = dy[d] + y
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y] + 1
            shark.append((nx, ny))

print(max([max(r) for r in graph]) - 1)

