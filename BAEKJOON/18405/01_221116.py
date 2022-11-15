#단, 해당 위치에 바이러스가 존재하지 않는 경우 0이 주어진다. 또한 모든 바이러스의 번호는 K이하의 자연수로만 주어진다. 
#S초 뒤에 (X,Y)에 존재하는 바이러스의 종류를 출력한다. 만약 S초 뒤에 해당 위치에 바이러스가 존재하지 않는다면, 0을 출력한다.
# 왼쪽 위에 해당하는 곳은 (1,1)에 해당한다.
import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
graph = []
data = []
for x in range(n):
  col = list(map(int, input().split()))
  graph.append(col)
  for y in range(n):
    if col[y] != 0:
      data.append((col[y], 0, x, y))      

targetS, targetX, targetY = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

data.sort()
queue = deque(data)

while queue:
  v, s, x, y = queue.popleft()
  if s == targetS:
    break
  for d in range(4):
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
      graph[nx][ny] = v
      queue.append((v, s + 1, nx, ny))

print(graph[targetX - 1][targetY - 1])