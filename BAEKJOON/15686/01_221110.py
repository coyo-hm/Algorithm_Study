import itertools

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
#0은 빈 칸, 1은 집, 2는 치킨집
# 0 < 집 <= 2N
# 치킨집 >= m or 치킨집 <= 13
# 첫째 줄에 폐업시키지 않을 치킨집을 최대 M개를 골랐을 때, 도시의 치킨 거리의 최솟값을 출력한다.

home = []
chicken = []

for x in range(n):
  for y in range(n):
    if city[x][y] == 1:
      home.append((x, y))
    elif city[x][y] == 2:
      chicken.append((x, y))
ans = 2 * n * len(city)
for com in list(itertools.combinations(chicken, m)):
  l = 0
  for x, y in home:  
    l += min([abs(x - r) + abs(y - c) for r, c in com])
  ans = min(ans, l)

print(ans)