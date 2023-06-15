# https://school.programmers.co.kr/learn/courses/30/lessons/12905
def solution(board):
    max_leng = 0
    mx, my = len(board), len(board[0])
    dp = [[0] * (my + 1) for _ in range(mx + 1)]

    for x in range(1, mx + 1):
        for y in range(1, my + 1):
            if board[x - 1][y - 1] == 1:
                dp[x][y] = min(dp[x - 1][y], dp[x][y - 1], dp[x - 1][y - 1]) + 1
            max_leng = max(dp[x][y], max_leng)
    # print(dp, max_leng)

    return max_leng * max_leng