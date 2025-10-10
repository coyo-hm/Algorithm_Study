# https://school.programmers.co.kr/learn/courses/30/lessons/258705
# 1:03:31
def solution(n, tops):
    MOD = 10007
    dp = [[0] * 2 for _ in range(n)]

    dp[0][0] = 2 + tops[0]
    dp[0][1] = 1

    for i in range(1, n):

        dp[i][1] = (dp[i - 1][0] + dp[i - 1][1]) % MOD
        if tops[i]:
            dp[i][0] = (dp[i - 1][0] * 3 + dp[i - 1][1] * 2) % MOD
        else:
            dp[i][0] = (dp[i - 1][0] * 2 + dp[i - 1][1]) % MOD

    return (dp[-1][0] + dp[-1][1]) % MOD
