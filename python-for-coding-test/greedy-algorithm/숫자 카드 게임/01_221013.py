N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

result = max([min([graph[x][y] for y in range(M)]) for x in range(N)
])
print(result)