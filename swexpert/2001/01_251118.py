# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV5PzOCKAigDFAUq&probBoxId=AV9oaSMa3DEDFAQc&type=PROBLEM&problemBoxTitle=%5BD1%7ED2+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part2&problemBoxCnt=14
# 00:09:21

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split(" "))
    graph = [list(map(int, input().split(" "))) for _ in range(n)]
    ans = 0
    for r in range(n - m + 1):
        for c in range(n - m + 1):
            temp = 0
            for i in range(m):
                temp += sum(graph[r + i][c + j] for j in range(m))
            ans = max(temp, ans)
    print("#{0}".format(test_case), ans)
