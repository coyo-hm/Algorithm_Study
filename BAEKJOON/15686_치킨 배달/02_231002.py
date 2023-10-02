import sys
from itertools import combinations

input = sys.stdin.readline
ans = int(1e9)
n, m = map(int, input().split())
cities = [list(map(int, input().split())) for _ in range(n)]
# 0은 빈 칸, 1은 집, 2는 치킨집

chicken = []
home = []

for r in range(n):
    for c in range(n):
        if cities[r][c] == 1:
            home.append((r, c))
        elif cities[r][c] == 2:
            chicken.append((r, c))

for chickens in combinations(chicken, m):
    dis = 0
    for hr, hc in home:
        dis += min([abs(hr - cr) + abs(hc - cc) for cr, cc in chickens])
    ans = min(dis, ans)

print(ans)