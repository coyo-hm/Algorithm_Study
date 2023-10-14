import sys
input = sys.stdin.readline
n = int(input())
students = [list(map(int, input().split())) for _ in range(n * n)]
graph = [[0] * n for _ in range(n)]
pos = []
ans = 0

dp = [0, 1, 10, 100, 1000]
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

for arr in students:
    std = arr[0]
    favs = arr[1:]
    pf, pe, pr, pc = 0, 0, n, n
    for r in range(n):
        for c in range(n):
            e, p = 0, 0
            if graph[r][c] == 0:
                for d in range(4):
                    nr = dr[d] + r
                    nc = dc[d] + c
                    if 0 <= nr < n and 0 <= nc < n:
                        if graph[nr][nc] in favs:
                            p += 1
                        elif graph[nr][nc] == 0:
                            e += 1
                if pf < p or (pf == p and pe < e) or (pf == p and pe == e and pr > r) or (pf == p and pe == e and pr == r and pc > c):
                    pf = p
                    pe = e
                    pr = r
                    pc = c
    graph[pr][pc] = std
    pos.append([std, pr, pc, favs])

for s, r, c, favs in pos:
    cnt = 0
    for d in range(4):
        nr = dr[d] + r
        nc = dc[d] + c
        if 0 <= nr < n and 0 <= nc < n and graph[nr][nc] in favs:
            cnt += 1
    ans += dp[cnt]

# print(graph)
print(ans)