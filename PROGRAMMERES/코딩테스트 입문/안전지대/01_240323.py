# https://school.programmers.co.kr/learn/courses/30/lessons/120866
def solution(board):
    answer = 0
    n = len(board)
    for r in range(n):
        for c in range(n):
            if board[r][c] == 1:
                for i in range(max(0, r - 1), min(n, r + 2)):
                    for j in range(max(0, c - 1), min(n, c + 2)):
                        if board[i][j] != 1:
                            board[i][j] = 2

    for row in board:
        # print(row)
        answer += row.count(0)
    return answer