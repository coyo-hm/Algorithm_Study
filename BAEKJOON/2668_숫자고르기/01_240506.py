# https://www.acmicpc.net/problem/2668
# 00:44:47


import sys

input = sys.stdin.readline

n = int(input())

graph = [0] + [int(input()) for _ in range(n)]
answer = []


def dfs(target, start, visited):
    visited[target] = True
    nex = graph[target]
    if not visited[nex]:
        dfs(nex, start, visited)
    elif nex == start:
        answer.append(nex)


for i in range(1, n + 1):
    visited = [False] * (n + 1)
    dfs(i, i, visited)

# answer.sort()
print(len(answer))
for i in answer:
    print(i)
