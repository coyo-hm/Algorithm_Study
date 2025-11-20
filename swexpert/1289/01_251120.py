# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV19AcoKI9sCFAZN&probBoxId=AV-4MojKLNADFATz&type=PROBLEM&problemBoxTitle=%5BD2%7ED3+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part4&problemBoxCnt=14
# 00:13:53

T = int(input())
for test_case in range(1, T + 1):
    memory = list(map(int, input().rstrip()))
    curr, cnt = 0, 0
    for n in memory:
        if curr != n:
            curr = n
            cnt += 1
    print("#{0}".format(test_case), cnt)
