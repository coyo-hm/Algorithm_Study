# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV5LrsUaDxcDFAXc&probBoxId=AV9gdM_anw0DFAQc&type=PROBLEM&problemBoxTitle=%5BD1%7ED2+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part1&problemBoxCnt=20
# 00:16:59

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    prices = list(map(int, input().split(" ")))
    profit = 0
    m = prices[-1]
    for i in range(n - 2, -1, -1):
        if m > prices[i]:
            profit += m - prices[i]
        else:
            m = prices[i]
    print("#{0}".format(test_case), profit)