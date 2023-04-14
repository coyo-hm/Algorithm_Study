from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(board, dir):
    n = len(board)
    price = [[int(1e9)] * n for _ in range(n)]
    price[0][0] = 0
    q = deque([(0, 0, 0, dir)])

    while q:
        x, y, c, d = q.popleft()
        # print(q)
        if x == n - 1 and y == n - 1:
            continue

        for nd in range(4):
            nx = x + dx[nd]
            ny = y + dy[nd]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 1:
                nc = c + 100 if nd == d else c + 600
                if nc < price[nx][ny]:
                    price[nx][ny] = nc
                    q.append((nx, ny, nc, nd))
    # print(price)
    return price[-1][-1]

def solution(board):
    print(bfs(board, 0), bfs(board, 1))
    return min(bfs(board, 0), bfs(board, 1))