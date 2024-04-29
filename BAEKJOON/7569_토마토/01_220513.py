# https://www.acmicpc.net/problem/7569

import collections
from functools import reduce
import sys

M, N, H = map(int, input().split())
box = []
q = collections.deque([])
total = M * N * H
alreadyRiper = 0

for i in range(H):
  b = []
  for j in range(N):
    # line = list(map(int, input().split()))
    line = list(map(int, sys.stdin.readline().split()))
    b.append(line)
    for k in range(M):
      if(line[k] == 1):
        q.append((i, j, k))      
  box.append(b)

dh = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]

while q:
  h, x, y = q.popleft()      
  for i in range(6):
    nh, nx, ny = h + dh[i], x + dx[i], y + dy[i]
    if(0 <= nh < H and 0 <= nx < N and 0 <= ny < M):
      if(box[nh][nx][ny] == 0):
        box[nh][nx][ny] = box[h][x][y] + 1
        q.append((nh, nx, ny))          

nonRiper = reduce(lambda x, y: x + y, [box[i][j].count(0) for i in range(H) for j in range(N)])
day = max([max(box[i][j]) for i in range(H) for j in range(N)])
if nonRiper == 0: print(day - 1)
else: print(-1)