def solution(n, l, r):
    answer = 0
    # dp = ["1"] * 21
    # n = 4
    # for i in range(1, n + 1):
    #     dp[i] = dp[i - 1].replace("0", "00000").replace("1","11011")
    # print(dp[n])
    for i in range(l - 1, r):
        # print(i, i % 5, i // (5 ** (n - 1)), (i // 5) % 5)
        if i % 5 != 2 and i // (5 ** (n - 1)) != 2 and (i // 5) % 5 != 2:
            answer += 1
    return answer