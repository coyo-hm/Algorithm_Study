# https://softeer.ai/practice/6247
# https://youtu.be/PAihI2CGr-M?si=Gf12VINr4jnsGH4L
# 01:30:10

import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
adjR = [[] for _ in range(n + 1)]
answer = 0

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adjR[b].append(a)

s, t = map(int, input().split())  # 동환이의 집과 회사의 위치에 해당하는 정점 번호 S와 T


def dfs(curr, adj, visit):
    if visit[curr]:
        return
    visit[curr] = True
    for neighbor in adj[curr]:
        dfs(neighbor, adj, visit)
    return


fromS = [False] * (n + 1)
fromS[t] = True
dfs(s, adj, fromS)
toS = [False] * (n + 1)
dfs(s, adjR, toS)
fromT = [False] * (n + 1)
fromT[s] = True
dfs(t, adj, fromT)
toT = [False] * (n + 1)
dfs(t, adjR, toT)

for i in range(1, n + 1):
    if fromS[i] and toS[i] and fromT[i] and toT[i]:
        answer += 1

print(answer - 2)
# print(len(answer))
