import collections


def find(maps):
    s = False
    l = False
    e = False

    for x in range(len(maps)):
        for y in range(len(maps[0])):
            if maps[x][y] == "S":
                s = (x, y)
            elif maps[x][y] == "L":
                l = (x, y)
            elif maps[x][y] == "E":
                e = (x, y)
            if s != False and l != False and e != False:
                return [s, l, e]


def distance(maps, start, end):
    graph = [[0] * len(maps[0]) for _ in range(len(maps))]
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    q = collections.deque([start])
    [ex, ey] = end

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                continue
            if nx == ex and ey == ny:
                return graph[x][y] + 1
            elif maps[nx][ny] != "X" and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
    return -1


def solution(maps):
    [s, l, e] = find(maps)
    answer = 0
    SToL = distance(maps, s, l)
    LToE = distance(maps, l, e)
    # print(SToL, LToE)

    return SToL + LToE if SToL >= 0 and LToE >= 0 else -1