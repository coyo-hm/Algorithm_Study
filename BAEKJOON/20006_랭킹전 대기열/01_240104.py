# https://www.acmicpc.net/problem/20006
# 00:20:26

import sys

input = sys.stdin.readline
p, m = map(int, input().split())
rooms = []
users = {}

for _ in range(p):
    level, nickname = input().rstrip().split()
    level = int(level)
    is_entered = False
    users[nickname] = level

    for r in range(len(rooms)):
        host_level = users[rooms[r][0]]
        if len(rooms[r]) < m and host_level - 10 <= level <= host_level + 10:
            rooms[r].append(nickname)
            is_entered = True
            break

    if not is_entered:
        rooms.append([nickname])

for room in rooms:
    print("Waiting!" if len(room) < m else "Started!")
    for user in sorted(room):
        print(users[user], user)
