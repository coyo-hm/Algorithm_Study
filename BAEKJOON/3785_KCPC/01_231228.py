# https://www.acmicpc.net/problem/3758
# 00:57:27

import sys

input = sys.stdin.readline


def solution():
    n, k, selected__team_id, m = map(int, input().split())
    teams = [[0, 0, 0, i] for i in range(n + 1)]
    problems = [[0] * (n + 1) for _ in range(k + 1)]

    for t in range(m):
        team_id, problem_id, curr_score = map(int, input().split())
        teams[team_id][1] += 1
        teams[team_id][2] = t + 1
        score = max(problems[problem_id][team_id], curr_score)
        teams[team_id][0] = teams[team_id][0] - problems[problem_id][team_id] + score
        problems[problem_id][team_id] = score

    teams = sorted(teams[1:], key=lambda x: [-x[0], x[1], x[2]])
    rank = 1
    for t in teams:
        if t[3] == selected__team_id:
            print(rank)
        else:
            rank += 1


for _ in range(int(input())):
    solution()
