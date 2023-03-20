import sys
from collections import deque

input = sys.stdin.readline
cycle = []

for _ in range(4):
  cycle.append(deque(input().replace("\n","")))
k = int(input())


for _ in range(k):
  rc, rd = map(int, input().split())
  rc -= 1
  link = []
  for i in range(4):
      link.append([cycle[i][6], cycle[i][2]])
  if rc != 0:
    for i in range(rc, 0, -1):
      if link[i][0] != link[i - 1][1]:
        if (rc - i + 1) % 2 == 0:
          cycle[i - 1].rotate(rd)
        else:
          cycle[i - 1].rotate(-1 * rd)
      else:
        break
  if rc != 3:
    for i in range(rc, 3):
      if link[i][1] != link[i + 1][0]:
        if (rc - i - 1) % 2 == 0:
          cycle[i + 1].rotate(rd)
        else:
          cycle[i + 1].rotate(-1 * rd)
      else:
        break
  cycle[rc].rotate(rd)

ans = 0
if cycle[0][0] == "1":
  ans += 1
if cycle[1][0] == "1":
  ans += 2
if cycle[2][0] == "1":
  ans += 4
if cycle[3][0] == "1":
  ans += 8
print(ans)