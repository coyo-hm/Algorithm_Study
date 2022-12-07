import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n, m = map(int, input().split())
  graph = list(map(int, input().split()))
  leng = n * m
  dp = [0] * (n)
  for i in range(n):
    dp[i] = graph[i * m]
    x = i
    for j in range(1, m):
      a = (x - 1) * m + j
      b = x * m + j
      c = (x + 1) * m + j
      p = max([graph[idx] for idx in [a, b, c] if 0 <= idx < leng])
      
      dp[i] += p
      if 0 <= a < leng and p == graph[a]:
        x -= 1
      elif 0 <= c < leng and p == graph[c]:
        x += 1
  print(max(dp))