# https://www.acmicpc.net/problem/1149

import sys

input = sys.stdin.readline
n = int(input())
home = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * 3 for _ in range(n)]
dp[0] = home[0]

for i in range(1, n):
    dp[i][0] = home[i][0] + min(dp[i - 1][1], dp[i - 1][2])
    dp[i][1] = home[i][1] + min(dp[i - 1][0], dp[i - 1][2])
    dp[i][2] = home[i][2] + min(dp[i - 1][0], dp[i - 1][1])

print(min(dp[n - 1]))
