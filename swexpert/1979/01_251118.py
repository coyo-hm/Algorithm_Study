# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV5PuPq6AaQDFAUq&probBoxId=AV9oaSMa3DEDFAQc&type=PROBLEM&problemBoxTitle=%5BD1%7ED2+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part2&problemBoxCnt=14
# 00:54:46

T = int(input())
for test_case in range(1, T + 1):
    cnt = 0
    n, k = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(n)]
    drc = [(0, 1), (1, 0)]
    for a in range(n):
        for b in range(n - k + 1):
            is_able_row = True
            is_able_col = True
            for c in range(k):
                if puzzle[a][b + c] == 0:
                    is_able_col = False
                if puzzle[b + c][a] == 0:
                    is_able_row = False
            if is_able_col and (b + k >= n or puzzle[a][b + k] == 0) and (b == 0 or puzzle[a][b - 1] == 0):
                cnt += 1
            if is_able_row and (b + k >= n or puzzle[b + k][a] == 0) and (b == 0 or puzzle[b - 1][a] == 0):
                cnt += 1




    print("#{0}".format(test_case), cnt)
