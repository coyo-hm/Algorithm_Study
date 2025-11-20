# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV14hwZqABsCFAYD&probBoxId=AV-4MojKLNADFATz&type=PROBLEM&problemBoxTitle=%5BD2%7ED3+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part4&problemBoxCnt=14
# 00:45:10

T = 10
for test_case in range(1, T + 1):
    N = int(input())
    graph = [input().split() for _ in range(N)]
    cnt = 0
    for c in range(N):
        col = "".join([graph[r][c] for r in range(N) if graph[r][c] != "0"])
        col = col.lstrip("2")
        col = col.rstrip("1")
        cnt += col.count("12")
    print("#{0}".format(test_case), cnt)
