import sys
input = sys.stdin.readline
n = int(input())
chart = [map(int, input().split()) for i in range(n)]
dp = [0] * (n + 2)

for i in range(n, 0, -1):
    [t, p] = chart[i - 1]
    # print(i, dp)
    if i + t <= n + 1:
        dp[i] = max(dp[i + 1], dp[i + t] + p)
    else:
        dp[i] = dp[i + 1]

print(dp[1])