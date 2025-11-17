# https://www.acmicpc.net/problem/13460
# 00::53:40

from collections import deque

n, m = map(int, input().split(" "))
graph = []
rr, rc, br, bc = 0, 0, 0, 0
drc = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for r in range(n):
    row = input().rstrip()
    graph.append(row)
    for c in range(m):
        if row[c] == "B":
            br, bc = r, c
        if row[c] == "R":
            rr, rc = r, c


def solution(rr, rc, br, bc):
    queue = deque([(rr, rc, br, bc, 0)])
    visited = [(rr, rc, br, bc)]
    while queue:
        rr, rc, br, bc, cnt = queue.popleft()
        if cnt > 10:
            return -1
        if graph[rr][rc] == "O":
            return cnt
        for dr, dc in drc:
            nrr, nrc = rr, rc
            while True:
                nrr += dr
                nrc += dc
                if graph[nrr][nrc] == "#":
                    nrr -= dr
                    nrc -= dc
                    break
                if graph[nrr][nrc] == "O":
                    break

            nbr, nbc = br, bc
            while True:
                nbr += dr
                nbc += dc
                if graph[nbr][nbc] == "#":
                    nbr -= dr
                    nbc -= dc
                    break
                if graph[nbr][nbc] == "O":
                    break

            if graph[nbr][nbc] == "O":
                continue
            if nrr == nbr and nrc == nbc:
                if abs(nrc - rc) + abs(nrr - rr) > abs(nbc - bc) + abs(nbr - br):
                    nrr -= dr
                    nrc -= dc
                else:
                    nbr -= dr
                    nbc -= dc
            if (nrr, nrc, nbr, nbc) not in visited:
                queue.append((nrr, nrc, nbr, nbc, cnt + 1))
                visited.append((nrr, nrc, nbr, nbc))

    return -1


print(solution(rr, rc, br, bc))
