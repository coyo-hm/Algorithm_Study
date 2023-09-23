import sys

sys.setrecursionlimit(500000)

DIR = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
answer = []


def calcMove(x, y, n, m):
    return (x % n, y % m)


def calcDir(cur, d):
    if cur == "S":
        return d
    elif cur == "R":
        return (d + 1) % 4
    else:
        return (d - 1) % 4


def search(r, c, d, er, ec, ed, visited, grid, cnt, n, m):
    visited[(r, c, d)] = True
    cnt += 1
    dr, dc = DIR[d]
    nr, nc = calcMove(r + dr, c + dc, n, m)
    nd = calcDir(grid[nr][nc], d)

    if (nr, nc, nd) == (er, ec, ed):
        answer.append(cnt)
    else:
        search(nr, nc, nd, er, ec, ed, visited, grid, cnt, n, m)
        return


def solution(grid):
    n, m = len(grid), len(grid[0])
    visited = {}
    for r in range(n):
        for c in range(m):
            for d in range(4):
                if (r, c, d) not in visited:
                    search(r, c, d, r, c, d, visited, grid, 0, n, m)
    answer.sort()
    return answer