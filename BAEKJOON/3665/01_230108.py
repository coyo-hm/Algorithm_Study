import sys
from collections import deque

input = sys.stdin.readline

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

for _ in range(int(input())):
  n = int(input())
  prevRank = list(map(int, input().split()))
  indegree = [0] * (n + 1)
  graph = [[False] * (n + 1) for i in range(n + 1)]

  for i in range(n):
    for j in range(i + 1, n):
      graph[prevRank[i]][prevRank[j]] = True
      indegree[prevRank[j]] += 1

  m = int(input())
  for i in range(m):
    a, b = map(int, input().split())
    if graph[a][b]:
      graph[a][b] = False
      graph[b][a] = True
      indegree[a] += 1
      indegree[b] -= 1
    else:
      graph[a][b] = True
      graph[b][a] = False
      indegree[a] -= 1
      indegree[b] += 1

  result = []
  q = deque()

  for i in range(1, n + 1):
    if indegree[i] == 0:
      q.append(i)

  certain = True
  cycle = False

  for i in range(n):
    if len(q) == 0:
      cycle = True
      break
    if len(q) >= 2:
      certain = False
      break
    now = q.popleft()
    result.append(now)
    for j in range(1, n + 1):
      if graph[now][j]:
        indegree[j] -= 1
        if indegree[j] == 0:
          q.append(j)

  if cycle:
    print("IMPOSSIBLE")
  elif not certain:
    print("?")
  else:
    for i in result:
      print(i, end = " ")
    print()
  