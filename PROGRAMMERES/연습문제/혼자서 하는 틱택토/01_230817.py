# - [혼자서 하는 틱택토](https://school.programmers.co.kr/learn/courses/30/lessons/160585)

def check(board, visited, sx, sy):
    dx = [1, -1, 0, 0, -1, 1, -1, 1]
    dy = [0, 0, 1, -1, -1, 1, 1, -1]
    visited[sx][sy] = True
    for d in range(8):
        cnt = 1
        for i in range(1, 3):
            nx, ny = dx[d] * i + sx, sy + dy[d] * i
            if nx < 0 or nx >= 3 or ny < 0 or ny >= 3 or board[sx][sy] != board[nx][ny]:
                continue
            cnt += 1
        if cnt == 3:
            return True
    return False


def solution(board):
    board = [list(row) for row in board]
    visited = [[False] * 3 for _ in range(3)]
    cnt_O, cnt_X = 0, 0
    win_O, win_X = 0, 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == "O":
                cnt_O += 1
                if visited[i][j] == False:
                    if check(board, visited, i, j):
                        win_O += 1
            elif board[i][j] == "X":
                cnt_X += 1
                if visited[i][j] == False:
                    if check(board, visited, i, j):
                        win_X += 1

    if cnt_O - cnt_X < 0 or cnt_O - cnt_X > 1:
        return 0
    if win_X > 0 and win_O > 0:
        return 0
    if win_X > 0 and cnt_O != cnt_X:
        return 0
    if win_O > 0 and cnt_X + 1 != cnt_O:
        return 0
    return 1