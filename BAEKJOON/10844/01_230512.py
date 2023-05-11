import sys

input = sys.stdin.readline
n = int(input())
dp = [[0] * 10 for _ in range(101)]
dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, n + 1):
    for j in range(10):
        temp = 0
        if j > 0:
            temp += dp[i - 1][j - 1]
        if j < 9:
            temp += dp[i - 1][j + 1]
        dp[i][j] = temp

# print(dp[:n + 1])
print(sum(dp[n]) % 1000000000)