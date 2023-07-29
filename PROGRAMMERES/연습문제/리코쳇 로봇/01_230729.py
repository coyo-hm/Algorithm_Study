from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
INF = int(1e9)

def bfs(board, sx, sy):
    rn = len(board)
    cn = len(board[0])
    count = [[INF] * cn for _ in range(rn)]
    count[sx][sy] = 0
    q = deque([(sx, sy, 0)])
    while q:
        x, y, s = q.popleft()
        for d in range(4):
            nx = x
            ny = y
            while 0 <= nx + dx[d] < rn and 0 <= ny + dy[d] < cn and board[nx + dx[d]][ny + dy[d]] != "D":
                nx += dx[d]
                ny += dy[d]
            if 0 <= nx < rn and 0 <= ny < cn and s + 1 < count[nx][ny]:
                count[nx][ny] = s + 1
                if board[nx][ny] == "G":
                    return s + 1
                q.append((nx, ny, s + 1))
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