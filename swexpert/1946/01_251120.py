# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV5PmkDKAOMDFAUq&probBoxId=AV-HZfeqN3ADFASP&type=PROBLEM&problemBoxTitle=%5BD2%7ED3+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part3&problemBoxCnt=14
# 00:08:20

WIDTH = 10

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    answer = ""
    for i in range(n):
        c, cnt = input().split()
        cnt = int(cnt)
        answer += c * cnt
    print("#{0}".format(test_case))
    for i, c in enumerate(list(answer)):
        print(c, end="")
        if i % WIDTH == 9 and i != len(answer) - 1:
            print()
    print()