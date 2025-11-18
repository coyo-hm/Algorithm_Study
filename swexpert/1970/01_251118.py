# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV5PsIl6AXIDFAUq&probBoxId=AV9oaSMa3DEDFAQc&type=PROBLEM&problemBoxTitle=%5BD1%7ED2+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part2&problemBoxCnt=14
# 00:08:00

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    cnt = []
    for i, m in enumerate(money):
        cnt.append(n // m)
        n = n % m

    print("#{0}".format(test_case))
    print(" ".join(map(str, cnt)))
