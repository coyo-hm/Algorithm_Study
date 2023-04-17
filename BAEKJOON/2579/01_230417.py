import sys

input = sys.stdin.readline

n = int(input())
s = [int(input()) for _ in range(n)]
dp = [0] * 301
dp[0] = s[0]


if n > 1:
  dp[1] = s[1] + s[0]

if n > 3:
  dp[2] = max(s[0], s[1]) + s[2]
  for i in range(3, n):
    dp[i] = s[i] + max(dp[i - 3] + s[i - 1], dp[i - 2])


print(dp[n-1])
