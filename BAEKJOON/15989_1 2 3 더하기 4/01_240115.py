# https://www.acmicpc.net/problem/15989
# 2:08:11

import sys

input = sys.stdin.readline
m = 100001
dp = [1] * m

for i in range(2, m):
    dp[i] += dp[i - 2]

for i in range(3, m):
    dp[i] += dp[i - 3]

t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n])
