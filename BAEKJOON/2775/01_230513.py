import sys
input = sys.stdin.readline

t = int(input())
dp = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]]

for i in range(1, 15):
    temp = [0]
    res = 0
    for j in range(1, 15):
        res += dp[i - 1][j]
        temp.append(res)
    dp.append(temp)

for _ in range(t):
    k = int(input())
    n = int(input())
    print(dp[k][n])