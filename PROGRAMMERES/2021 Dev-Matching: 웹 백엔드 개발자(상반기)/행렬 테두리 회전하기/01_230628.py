def rotate(sx, sy, ex, ey, graph):
    m = int(INF)
    t = graph[sx - 1][sy]
    for y in range(sy - 1, ey - 1):
        graph[]

    for x in range(sx, ex - 1):
        for y


def solution(rows, columns, queries):
    answer = []
    graph = [[c + r * rows + 1 for c in range(columns)] for r in range(rows)]
    print(graph)
    return answer