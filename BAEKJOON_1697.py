import collections

N, K = map(int, input().split())
graph = [0] * (10**5 + 1)

def bfs(v):
  q = collections.deque([v])
  graph[v] = 1
  while q:
    node = q.popleft()
    if(node == K): return (graph[node] - 1)
    for i in (node * 2, node + 1, node - 1):
      if 0 <= i <(10**5 + 1) and graph[i] == 0:
        graph[i] = graph[node] + 1
        q.append(i)

print(bfs(N))