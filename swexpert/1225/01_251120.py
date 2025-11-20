# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV14uWl6AF0CFAYD&probBoxId=AV-4MojKLNADFATz&type=PROBLEM&problemBoxTitle=%5BD2%7ED3+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part4&problemBoxCnt=14
# 00:12:06

from collections import deque

T = 10
for _ in range(1, T + 1):
    test_case = int(input())
    data = deque(map(int, input().split()))
    cnt = 0
    while True:
        n = max(data.popleft() - cnt - 1, 0)
        data.append(n)
        if n == 0:
            break
        cnt = (cnt + 1) % 5
    print("#{0}".format(test_case), " ".join(map(str, data)))
