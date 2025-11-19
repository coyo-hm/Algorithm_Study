# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV13_BWKACUCFAYh&probBoxId=AV-HZfeqN3ADFASP&type=PROBLEM&problemBoxTitle=%5BD2%7ED3+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part3&problemBoxCnt=14
# 00:36:55

UNIT = 100

for _ in range(10):
    grid, answer = [], []
    n = int(input())
    for _ in range(UNIT):
        row = list(map(int, input().split()))
        grid.append(row)
        answer.append(sum(row))
    cross_sum = [0, 0]
    for i in range(UNIT):
        col_sum = 0
        cross_sum[0] += grid[i][i]
        cross_sum[1] += grid[i][UNIT - i - 1]
        for j in range(UNIT):
            col_sum += grid[j][i]
        answer.append(col_sum)
    answer += cross_sum
    print("#{0}".format(n), max(answer))
