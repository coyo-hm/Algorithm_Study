# https://www.acmicpc.net/problem/3758
# 00:20:20

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k, t, m = map(int, input().split())
    teams = [[0, 0, 0, i + 1] for i in range(n)]
    quiz = [[0] * n for _ in range(k)]
    for order in range(m):
        team_id, quiz_id, score = map(int, input().split())
        team_id, quiz_id = team_id - 1, quiz_id - 1
        teams[team_id][1] += 1
        teams[team_id][2] = order
        if score > quiz[quiz_id][team_id]:
            teams[team_id][0] = teams[team_id][0] - quiz[quiz_id][team_id] + score
            quiz[quiz_id][team_id] = score

    teams.sort(key=lambda x: [-x[0], x[1], x[2]])
    for rank, team in enumerate(teams):
        if team[3] == t:
            print(rank + 1)
            break
