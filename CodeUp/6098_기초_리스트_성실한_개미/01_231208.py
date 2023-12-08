graph = [list(map(int, input().split())) for _ in range(10)]
r, c = 1, 1
while True:
    if graph[r][c] == 2:
        graph[r][c] = 9
        break
    graph[r][c] = 9
    if c + 1 < 10 and graph[r][c + 1] == 0 or graph[r][c + 1] == 2:
        c += 1
    elif r + 1 < 10 and graph[r + 1][c] == 0 or graph[r + 1][c] == 2:
        r += 1
    else:
        break

for r in range(10):
    print(" ".join([str(i) for i in graph[r]]))