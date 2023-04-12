def solution(dirs):
    answer = 0
    dir = {
        "U":(1, 0),
        "D":(-1, 0),
        "R":(0, 1),
        "L":(0, -1),
    }
    route = []
    x = 0
    y = 0

    for d in dirs:
        dy, dx = dir[d]
        nx = x + dx
        ny = y + dy
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            if ((y, x), (ny, nx)) not in route and ((ny, nx), (y, x)) not in route:
                answer += 1
            route.append(((y, x), (ny, nx)))
            y = ny
            x = nx

    return answer