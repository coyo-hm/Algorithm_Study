a, m, d, n = map(int, input().split())
dp = [0] * (n + 1)
dp[1] = a
for i in range(2, n + 1):
    dp[i] = dp[i - 1] * m + d
print(dp[n])