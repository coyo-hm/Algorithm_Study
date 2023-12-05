import sys
input = sys.stdin.readline

def solution(teams):
    team_cnt = {}
    team = {}
    for rank, t in enumerate(teams):
        if t in team_cnt:
            team_cnt[t] += 1
        else:
            team_cnt[t] = 1

    score = 1
    for t in teams:
        if team_cnt[t] < 6:
            continue
        if t in team:
            team[t].append(score)
        else:
            team[t] = [score]
        score += 1

    winner = list(team.keys())[0]
    for t, arr in team.items():
        winner_score = sum(team[winner][:4])
        curr_score = sum(arr[:4])
        if winner_score > curr_score:
            winner = t
        elif winner_score == curr_score and team[winner][4] > arr[4]:
            winner = t

    print(winner)


T = int(input())
for _ in range(T):
    N = int(input())
    teams = list(map(int, input().split()))
    solution(teams)


