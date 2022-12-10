import sys
input = sys.stdin.readline

n = int(input())
t = []
p = []

DP = [0] * (n + 1)
ans = 0

for _ in range(n):
  i, j = map(int, input().split())
  t.append(i)
  p.append(j)

for i in range(n -1, -1, -1):
  time = t[i] + i
  if time <= n:
    DP[i] = max(p[i] + DP[time], ans)
    ans = DP[i]
  else:
    DP[i] = ans

# print(DP)
print(ans)