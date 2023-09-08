import sys
import collections

input = sys.stdin.readline
rl, cl = map(int, input().split())
graph = [list(input())[:-1] for _ in range(rl)]
visited = [[False] * cl for _ in range(rl)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

fire = collections.deque([])
q = collections.deque([])

for r in range(rl):
    for c in range(cl):
        if graph[r][c] == "F":
            fire.append((r, c))
        elif graph[r][c] == "J":
            q.append((r, c, 0))
            visited[r][c] = True

def spreadFire(fire):
    newFire = collections.deque()
    while fire:
        fr, fc = fire.popleft()
        for d in range(4):
            nr = dr[d] + fr
            nc = dc[d] + fc
            if 0 <= nr < rl and 0 <= nc < cl and graph[nr][nc] != "#"  and graph[nr][nc] != "F":
                graph[nr][nc] = "F"
                newFire.append((nr, nc))
    return newFire
def bfs(q, fire, graph, visited):
    prevCnt = 0
    fire.extend(spreadFire(fire))
    while q:
        r, c, cnt = q.popleft()
        if prevCnt < cnt:
            fire.extend(spreadFire(fire))
            prevCnt = cnt
        for d in range(4):
            nr = dr[d] + r
            nc = dc[d] + c
            if nr < 0 or nr >= rl or nc < 0 or nc >= cl:
                return cnt + 1
            elif 0 <= nr < rl and 0 <= nc < cl and graph[nr][nc] == "." and visited[nr][nc] == False:
                q.append((nr, nc, cnt + 1))
                visited[nr][nc] = True



    return "IMPOSSIBLE"



ans = bfs(q, fire, graph, visited)
print(ans)