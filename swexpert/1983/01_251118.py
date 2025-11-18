# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV5PwGK6AcIDFAUq&probBoxId=AV9oaSMa3DEDFAQc&type=PROBLEM&problemBoxTitle=%5BD1%7ED2+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part2&problemBoxCnt=14
# 00:22:00

UNIT = 10
GRADE = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    scores = []
    for i in range(n):
        mid, fin, ass = map(int, input().split())
        score = mid * 0.35 + fin * 0.45 + ass * 0.2
        scores.append((score, i + 1))
    scores.sort(key=lambda x: (-x[0], x[1]))
    for g, (s, i) in enumerate(scores):
        if i == k:
            temp = int(g // (n / UNIT))
            grade = GRADE[temp]
            print("#{0}".format(test_case), grade)
            break
