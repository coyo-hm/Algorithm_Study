def calcDis(x1, y1, x2, y2):
    return int((x1 - x2) ** 2 + (y1 - y2) ** 2)

def minDis(m, n, startX, startY, endX, endY):
    INF = float('inf')
    u, d, l, r = INF, INF, INF, INF
    if not(startX == endX and startY < endY):
        u = calcDis(startX, startY, endX, 2 * n - endY)
    if not(startX == endX and startY > endY):
        d = calcDis(startX, startY, endX, -endY)
    if not(startX > endX and startY == endY):
        l = calcDis(startX, startY, -endX, endY)
    if not(startX < endX and startY == endY):
        r = calcDis(startX, startY, 2 * m - endX, endY)
    return min(u, d, l, r)

def solution(m, n, startX, startY, balls):
    answer = [minDis(m, n, startX, startY, endX, endY) for [endX, endY] in balls]
    return answer