# https://www.acmicpc.net/problem/13460
# 01:31:01

import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
board = []
dyx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ry, rx, by, bx = 0, 0, 0, 0

for y in range(n):
    temp = list(input().rstrip())
    for x in range(m):
        if temp[x] == "R":
            ry, rx = y, x
        elif temp[x] == "B":
            by, bx = y, x
    board.append(temp)


def solution(ry, rx, by, bx):
    q = deque([(ry, rx, by, bx, 0)])
    visited = [(ry, rx, by, bx)]
    while q:
        ry, rx, by, bx, cnt = q.popleft()
        if cnt > 10:
            print(-1)
            return
        if board[ry][rx] == "O":
            print(cnt)
            return

        for dy, dx in dyx:
            nry, nrx = ry, rx
            while True:
                nry += dy
                nrx += dx
                if board[nry][nrx] == "#":
                    nry -= dy
                    nrx -= dx
                    break
                elif board[nry][nrx] == "O":
                    break
            nby, nbx = by, bx
            while True:
                nby += dy
                nbx += dx
                if board[nby][nbx] == "#":
                    nby -= dy
                    nbx -= dx
                    break
                elif board[nby][nbx] == "O":
                    break
            if board[nby][nbx] == "O":
                continue
            if nry == nby and nrx == nbx:
                if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):
                    nry -= dy
                    nrx -= dx
                else:
                    nby -= dy
                    nbx -= dx
            if (nry, nrx, nby, nbx) not in visited:
                q.append((nry, nrx, nby, nbx, cnt + 1))
                visited.append((nry, nrx, nby, nbx))
    print(-1)


solution(ry, rx, by, bx)
