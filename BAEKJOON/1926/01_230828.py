import sys
import collections
input = sys.stdin.readline

n, m = map(int, input().split())
painting = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
def find_painting(sr, sc):
    visited[sr][sc] = True
    q = collections.deque([(sr,sc)])
    s = 1

    while q:
        r, c = q.pop()
        for d in range(4):
            nr = dr[d] + r
            nc = dc[d] + c
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            if visited[nr][nc] == False and painting[nr][nc] == 1:
                visited[nr][nc] = True
                q.append((nr, nc))
                s += 1

    return s

maxS = 0
cnt = 0

for r in range(n):
    for c in range(m):
        if painting[r][c] == 1 and visited[r][c] == False:
            maxS = max(find_painting(r, c), maxS)
            cnt += 1

print(cnt)
print(maxS)
