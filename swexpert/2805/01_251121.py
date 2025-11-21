# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV7GLXqKAWYDFAXB&probBoxId=AV6kld8aiskDFASb&type=PROBLEM&problemBoxTitle=%EC%82%BC%EC%84%B1%EC%8B%9C%ED%97%98%EB%8C%80%EB%B9%84+%EA%B8%B0%EB%B3%B8%EB%AC%B8%EC%A0%9C%EB%AA%A8%EC%9D%8C%28%EB%82%9C%EC%9D%B4%EB%8F%84+1%7E3%29&problemBoxCnt=15
# 00:22:10

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, list(input().rstrip()))) for _ in range(N)]
    answer = 0
    mid = N // 2
    for r in range(mid):
        row = graph[r][mid - r:mid + r + 1]
        answer += sum(row)
    for r in range(mid, N):
        row = graph[r][mid - N + r + 1:mid + N - r]
        answer += sum(row)
    print("#{0}".format(test_case), answer)
