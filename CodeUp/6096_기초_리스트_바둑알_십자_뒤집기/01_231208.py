d = [list(map(int, input().split())) for _ in range(19)]
n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    for j in range(19):
        if d[j][y - 1] == 0:
            d[j][y - 1] = 1
        else:
            d[j][y - 1] = 0

        if d[x - 1][j] == 0:
            d[x - 1][j] = 1
        else:
            d[x - 1][j] = 0

for r in range(19):
    print(" ".join([str(i) for i in d[r]]))