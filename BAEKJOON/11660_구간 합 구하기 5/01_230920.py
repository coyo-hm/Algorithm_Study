import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dp = [[0] * (n + 1) for _ in range(n + 1)]
graph = [list(map(int, input().split())) for _ in range(n)]
cords = [map(int, input().split()) for _ in range(m)]

for x in range(1, n + 1):
    for y in range(1, n + 1):
        dp[x][y] = dp[x - 1][y] + dp[x][y - 1] - dp[x- 1][y - 1] + graph[x - 1][y - 1]

for (x1, y1, x2, y2) in cords:
    print(dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1])
