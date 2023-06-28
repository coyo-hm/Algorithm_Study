def rotate(sx, sy, ex, ey, graph):
    a = graph[sx][sy - 1]
    m = a
    for y in range(sy - 1, ey):
        b = graph[sx - 1][y]
        graph[sx - 1][y] = a
        a = b
        m = min(m, b)
    if len(graph) > 2:
        for x in range(sx, ex - 1):
            b = graph[x][ey - 1]
            graph[x][ey - 1] = a
            a = b
            m = min(m, b)
    for y in range(ey - 1, sy - 2, -1):
        b = graph[ex - 1][y]
        graph[ex - 1][y] = a
        a = b
        m = min(m, b)
    if len(graph) > 2:
        for x in range(ex - 2, sx - 2, -1):
            b = graph[x][sy - 1]
            graph[x][sy - 1] = a
            a = b
            m = min(m, b)
    # print(m)
    # for row in graph:
        # print(row)
    return [m, graph]

def solution(rows, columns, queries):
    answer = []
    graph = [[c + r * columns + 1 for c in range(columns)] for r in range(rows)]
    for sx, sy, ex, ey in queries:
        [m, graph] = rotate(sx, sy, ex, ey, graph)
        answer.append(m)
    return answer