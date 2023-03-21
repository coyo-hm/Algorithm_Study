import sys
import itertools

input = sys.stdin.readline
n = int(input())
ath = list(range(n))
graph = []
teams = itertools.combinations(ath, n // 2)
ans = 1e9

for _ in range(n):
  graph.append(list(map(int, input().split())))

def calc(t):
  t.sort()
  res = 0
  for i in range(n // 2 - 1):
    for j in range(i + 1, n // 2):
      res += graph[t[i]][t[j]] + graph[t[j]][t[i]]
  return res

for team in teams:
  a = calc(list(team))
  b = calc(list(set(ath) - set(team)))

  if abs(b - a) < ans:
    ans = abs(b - a)

print(ans)