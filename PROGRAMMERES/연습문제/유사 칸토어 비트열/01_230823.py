def solution(n, l, r):
    answer = 0
    dp = ["1"] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i - 1].replace("0", "00000").replace("1","11011")[:r]
    print(dp[n])
    return dp[n][l - 1:r].count("1")