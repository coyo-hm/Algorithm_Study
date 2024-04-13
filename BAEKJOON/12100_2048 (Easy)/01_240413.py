# https://www.acmicpc.net/problem/12100
# 01:43:39

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0


def solution(move, graph):
    global answer
    if move > 4:
        for row in graph:
            answer = max(answer, max(row))
        return

    graph_up = [[0] * n for _ in range(n)]
    graph_down = [[0] * n for _ in range(n)]
    graph_left = [[0] * n for _ in range(n)]
    graph_right = [[0] * n for _ in range(n)]

    for c in range(n):
        now = 0
        q = deque([graph[r][c] for r in range(0, n) if graph[r][c] != 0])
        if q:
            graph_up[now][c] = q.popleft()
        while q:
            com = q.popleft()
            if graph_up[now][c] == com:
                graph_up[now][c] *= 2
                graph_up[now + 1][c] = q.popleft() if q else 0
            else:
                graph_up[now + 1][c] = com
            now += 1

    for c in range(n):
        now = n - 1
        q = deque([graph[r][c] for r in range(n) if graph[r][c] != 0])
        if q:
            graph_down[now][c] = q.pop()
        while q:
            com = q.pop()
            if graph_down[now][c] == com:
                graph_down[now][c] *= 2
                graph_down[now - 1][c] = q.pop() if q else 0
            else:
                graph_down[now - 1][c] = com
            now -= 1

    for r in range(n):
        now = 0
        q = deque([graph[r][c] for c in range(n) if graph[r][c] != 0])
        if q:
            graph_left[r][now] = q.popleft()
        while q:
            com = q.popleft()
            if graph_left[r][now] == com:
                graph_left[r][now] *= 2
                graph_left[r][now + 1] = q.popleft() if q else 0
            else:
                graph_left[r][now + 1] = com
            now += 1

    for r in range(n):
        now = n - 1
        q = deque([graph[r][c] for c in range(n) if graph[r][c] != 0])
        if q:
            graph_right[r][now] = q.pop()
        while q:
            com = q.pop()
            if graph_right[r][now] == com:
                graph_right[r][now] *= 2
                graph_right[r][now - 1] = q.pop() if q else 0
            else:
                graph_right[r][now - 1] = com
            now -= 1

    solution(move + 1, graph_up)
    solution(move + 1, graph_down)
    solution(move + 1, graph_left)
    solution(move + 1, graph_right)


solution(0, board)

print(answer)
