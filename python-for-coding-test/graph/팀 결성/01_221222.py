import sys

input = sys.stdin.readline
n, m = map(int, input().split())
parent = [0] * (n + 1)

for i in range(n + 1):
  parent[i] = i

for _ in range(m):
  arth, a, b = map(int, input().split())
  if(arth == 0):
    if a > b:
      parent[b] = parent[a]
    else:
      parent[a] = parent[b]
  else:
    print("YES" if parent[a] == parent[b] else "NO")
  