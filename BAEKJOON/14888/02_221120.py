import sys

input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))
p, s, m, d = map(int, input().split())

min_value = 1e9
max_value = -1e9

def dfs(i, now):
  global min_value, max_value, p, s, m, d
  if i == n:
    min_value = min(min_value, now)
    max_value = max(max_value, now)
  else:
    if p > 0:
      p -= 1
      dfs(i + 1, now + data[i])
      p += 1
    if s > 0:
      s -= 1
      dfs(i + 1, now - data[i])
      s += 1
    if m > 0:
      m -= 1
      dfs(i + 1, now * data[i])
      m += 1
    if d > 0:
      d -= 1
      if now < 0:
        dfs(i + 1, -1 * (abs(now) // data[i]))
      else: 
        dfs(i + 1, now // data[i])
      d += 1

dfs(1, data[0])

print(max_value)
print(min_value)