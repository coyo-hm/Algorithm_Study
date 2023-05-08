import sys
import math
input = sys.stdin.readline
dp = [0] * 100001

n = int(input())

dp[1] = 1
dp[2] = 2
dp[3] = 3
dp[4] = 1

for i in range(5, n + 1):
    m = int(math.sqrt(i))
    # print(i, m, i - (m ** 2), [1 + dp[i - (j ** 2)] for j in range(1, m + 1)])
    dp[i] = min([1 + dp[i - (j ** 2)] for j in range(1, m + 1)])

# print(dp[:n+1])
print(dp[n])