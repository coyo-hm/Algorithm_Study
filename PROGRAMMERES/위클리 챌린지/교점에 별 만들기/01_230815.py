def solution(line):
    points = []
    l = len(line)
    INF = float("inf")
    wmin, wmax = INF, -INF
    hmin, hmax = INF, -INF
    for i in range(l):
        for j in range(i + 1, l):
            a, b, e, c, d, f = *line[i], *line[j]
            deno = a * d - b * c

            if deno == 0:
                continue

            y = (e * c - a * f) / deno
            x = (b * f - e * d) / deno

            if y != int(y) or x != int(x):
                continue
            y, x = int(y), int(x)
            points.append((y, x))
            wmin = min(wmin, x)
            wmax = max(wmax, x)
            hmin = min(hmin, y)
            hmax = max(hmax, y)

    answer = [["." for _ in range(wmax + 1 - wmin)] for _ in range(hmax + 1 - hmin)]
    for y, x in points: answer[hmax - y][x - wmin] = "*"
    return ["".join(row) for row in answer]