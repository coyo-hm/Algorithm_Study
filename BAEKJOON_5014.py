import collections
import sys

input = sys.stdin.readline
F, S, G, U, D = map(int, input().split())
graph = [0 for _ in range(F + 1)]
graph[S] = 1
q = collections.deque([S])
d = [U, -D]

while q:
  f = q.popleft()
  for i in range(2):
    df = f + d[i]
    if 0 < df <= F and graph[df] == 0:
      graph[df] = graph[f] + 1
      q.append(df)

print(graph[G] - 1 if graph[G] != 0 else "use the stairs")