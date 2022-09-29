from collections import deque

visited = []

def isSearch(m, n, board, sx, sy):
    dx = [0, 1, 1]
    dy = [1, 0, 1]
    c = board[sx][sy]
    visited[sx][sy] = True
    q = deque([(sx, sy)])
    for i in range(3):        
        nx, ny = dx + sx, dy + sy
        if 0 <= nx < m and 0 <= ny < n:
            for y in range(ny, -1, -1):
                print(nx, y)
                if c == board[nx][y] and visited[nx][y] == False:
                    print(nx, y)
                    q.append((nx, y))
                    visited[nx][y] = True
                    break
        else: 
            return []
    return q if len(q) == 4 else []

def solution(m, n, board):
    answer = 0
    visited = [[False for _ in range(m)] for _ in range(n)]
    # while True:
        plus = 0
        for i in range(m):
            for j in range(n):
                if visited[i][j] == False:
                    print(i, j)
                    
                    # plus += len(isSearch(m, n, board, i, j))
        # if plus == 0:
            # return answer
        # else: answer += plus
    return answer