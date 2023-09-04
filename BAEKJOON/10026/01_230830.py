import collections
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]

ans1, ans2 = 0, 0 #적록색약이 아닌 경우, 적록색약인 경우

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

visited1 = [[True] * n for _ in range(n)]
visited2 = [[True] * n for _ in range(n)]

def bfs1(sr, sc):
    q = collections.deque([(sr, sc)])
    visited1[sr][sc] = False

    while q:
        r, c = q.pop()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < n and graph[nr][nc] == graph[sr][sc] and visited1[nr][nc] == True:
                visited1[nr][nc] = False
                q.append((nr, nc))
def bfs2(sr, sc):
    q = collections.deque([(sr, sc)])
    visited2[sr][sc] = False


    while q:
        r, c = q.pop()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < n and (graph[nr][nc] == graph[sr][sc] or (graph[sr][sc] in ["R", "G"] and graph[nr][nc] in ["R", "G"])) and visited2[nr][nc] == True:
                visited2[nr][nc] = False
                q.append((nr, nc))

for sr in range(n):
    for sc in range(n):
        if visited1[sr][sc] == True:
            ans1 += 1
            bfs1(sr, sc)
        if visited2[sr][sc] == True:
            ans2 += 1
            bfs2(sr, sc)

print(ans1, ans2)