# https://www.acmicpc.net/problem/15990

import sys

input = sys.stdin.readline
t = int(input())
m = 100001
dp = [[0, 0, 0] for _ in range(m)]
dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]

for i in range(4, m):
    dp[i][0] = (dp[i - 1][1] + dp[i - 1][2]) % 1000000009
    dp[i][1] = (dp[i - 2][0] + dp[i - 2][2]) % 1000000009
    dp[i][2] = (dp[i - 3][0] + dp[i - 3][1]) % 1000000009

for _ in range(t):
    n = int(input())
    # print(dp[n])
    print(sum(dp[n]) % 1000000009)
