from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(board, sx, sy):
    rn = len(board)
    cn = len(board[0])
    q = deque([(sx, sy, 0, -1)])
    while q:
        x, y, s, pd = q.popleft()
        for d in range(0, 4):
            px, py = x, y
            if (0 == pd and d == 1) or (1 == pd and d == 0) or (2 == pd and d == 3) or (3 == pd and d == 2):
                continue
            for r in range(1, max(cn, rn)):
                nx = dx[d] * r + x
                ny = dy[d] * r + y
                if nx < 0 or nx >= rn or ny < 0 or ny >= cn or board[nx][ny] == "D":
                    if board[px][py] == "G":
                        return s
                    elif (px == x and py != y) or (px != x and py == y):
                        q.append((px, py, s + 1, d))
                    break
                else:
                    px, py = nx, ny
    return -1


def solution(board):
    rn = len(board)
    cn = len(board[0])
    board = [list(b) for b in board]

    for r in range(rn):
        for c in range(cn):
            if board[r][c] == "R":
                return bfs(board, r, c)

    return -1

solution([".D.R", "....", ".G..", "...D"]);