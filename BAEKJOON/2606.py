C = int(input())
L = int(input())
graph = [[] for _ in range(C+1)]
v = [False] * (C+1)
virus = []

for _ in range(L):
  a, b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(node):
  virus.append(node)
  v[node] = True
  for i in graph[node]:
    if(not v[i]): dfs(i)

dfs(1)
print(len(virus) - 1)