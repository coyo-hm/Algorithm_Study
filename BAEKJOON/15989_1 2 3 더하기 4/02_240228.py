# https://www.acmicpc.net/problem/15989
# 0:03:58

import sys

input = sys.stdin.readline
MAX_N = 10001
dp = [1] * MAX_N

for i in range(2, MAX_N):
    dp[i] += dp[i - 2]

for i in range(3, MAX_N):
    dp[i] += dp[i - 3]


for _ in range(int(input())):
    n = int(input())
    print(dp[n])