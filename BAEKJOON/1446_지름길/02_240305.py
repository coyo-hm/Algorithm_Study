# https://www.acmicpc.net/problem/1446
# 0:22:42

import sys

input = sys.stdin.readline
n, d = map(int, input().split())
roads = []

for _ in range(n):
    a, b, c = map(int, input().split())
    if b > d:
        continue
    roads.append([a, b, c])

roads.sort()


def drive(curr, idx, distance):
    if curr >= d or idx >= len(roads):
        return distance + d - curr
    min_distance = drive(curr, idx + 1, distance)
    s, e, c = roads[idx]
    if curr <= s:
        min_distance = min(min_distance, drive(e, idx + 1, distance + c + s - curr))
    return min_distance


print(drive(0, 0, 0))
