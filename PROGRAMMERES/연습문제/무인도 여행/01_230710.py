from collections import deque


def bfs(maps, visited, sx, sy, n, m):
    cnt = int(maps[sx][sy])
    visited[sx][sy] = True
    q = deque([(sx, sy)])

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny] == False and maps[nx][ny] != "X":
                q.append((nx, ny))
                visited[nx][ny] = True
                cnt += int(maps[nx][ny])
    return cnt


def solution(maps):
    answer = []
    rowSize = len(maps)
    colSize = len(maps[0])
    visited = [[False] * colSize for _ in range(rowSize)]

    for x in range(rowSize):
        for y in range(colSize):
            if maps[x][y] != "X" and visited[x][y] == False:
                res = bfs(maps, visited, x, y, rowSize, colSize)
                answer.append(res)

    answer.sort()

    return answer if len(answer) > 0 else [-1]