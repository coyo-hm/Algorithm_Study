# https://www.acmicpc.net/problem/20006
# 00:11:22

import sys

input = sys.stdin.readline
p, m = map(int, input().split())
player = {}
rooms = []

for _ in range(p):
    l, n = input().split()
    l = int(l)
    player[n] = l
    is_entered = False
    for room_idx in range(len(rooms)):
        room = rooms[room_idx]
        host_level = player[room[0]]
        if 0 < len(room) < m and host_level - 10 <= l <= host_level + 10:
            rooms[room_idx].append(n)
            is_entered = True
            break
    if not is_entered:
        rooms.append([n])

for room in rooms:
    print("Started!" if len(room) == m else "Waiting!")
    for n in sorted(room):
        print(player[n], n)
