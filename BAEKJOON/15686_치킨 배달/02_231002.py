import collections
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
cities = [list(map(int, input().split())) for _ in range(n)]
distance = [[0] * n for _ in range(n)]
# 0은 빈 칸, 1은 집, 2는 치킨집
def calcDis(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)

chicken = collections.deque([])
home = collections.deque([])

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

def bfs(sr, sc):
    visited = [[False] * n for _ in range(n)]
    q = collections.deque([(sr, sc)])
    global distance

    while q:
        r, c = q.popleft()
        dis = distance[r][c] if r != sr or c != sc else 0
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if nr < 0 or nr >= n or nc < 0 or nc >= n or visited[nr][nc]:
                continue
            distance[nr][nc] += dis + 1
            visited[nr][nc] = True
            q.append((nr, nc))

for r in range(n):
    for c in range(n):
        if cities[r][c] == 1:
            home.append((r, c))
            bfs(r, c)
        elif cities[r][c] == 2:
            chicken.append((r, c))

chicken_dis = [(distance[chicken[c][0]][chicken[c][1]], c) for c in range(len(chicken))]
chicken_dis.sort()

for hr, hc in home:
    for d, ci in chicken_dis[]:


print(chicken_dis)