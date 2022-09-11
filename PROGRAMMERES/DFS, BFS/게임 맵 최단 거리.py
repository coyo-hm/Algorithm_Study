import collections
def solution(maps):
    N = len(maps)    
    M = len(maps[0])
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    q = collections.deque([(0,0)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if(0 <= nx < N and 0 <= ny < M):
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    q.append((nx, ny))
    return maps[N - 1][M - 1] if maps[N - 1][M - 1] != 1 else -1