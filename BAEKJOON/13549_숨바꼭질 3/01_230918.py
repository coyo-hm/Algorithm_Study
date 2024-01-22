import sys
from collections import deque

N = 100001

input = sys.stdin.readline
n, k = map(int, input().split())
q = deque([])
q.append(n)
road = [int(1e9)] * N
visited = [True] * N
road[n] = 0

while q:
    p = q.popleft()
    visited[p] = False
    # print(p)
    if p + 1 < N and visited[p + 1] and road[p + 1] > road[p] + 1:
        road[p + 1] = road[p] + 1
        q.append(p + 1)
    if p > 0 and visited[p - 1] and road[p - 1] > road[p] + 1:
        road[p - 1] = road[p] + 1
        q.append(p - 1)
    if p * 2 < N and visited[p * 2] and road[p * 2] > road[p]:
        road[p * 2] = road[p]
        q.append(p * 2)

# print(road[min(n, k): max(n, k) + 1])
print(road[k])
