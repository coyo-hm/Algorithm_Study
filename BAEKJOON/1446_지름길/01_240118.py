# https://www.acmicpc.net/problem/1446
# 1:30:44

import sys

input = sys.stdin.readline
INF = int(1e9)

N, D = map(int, input().split())
roads = []

for _ in range(N):
    a, b, c = map(int, input().split())
    if b > D:
        continue
    roads.append([a, b, c])

roads.sort()


def ride(curr, idx, distance):
    if idx == len(roads) or curr >= D:
        return distance + D - curr
    min_distance = ride(curr, idx + 1, distance)
    s, e, c = roads[idx]
    if curr <= s:
        min_distance = min(min_distance, ride(e, idx + 1, distance + s - curr + c))
    return min_distance


answer = ride(0, 0, 0)
# print(roads)
print(answer)
