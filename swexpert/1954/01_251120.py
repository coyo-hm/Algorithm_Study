# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV5PobmqAPoDFAUq&probBoxId=AV-HZfeqN3ADFASP&type=PROBLEM&problemBoxTitle=%5BD2%7ED3+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part3&problemBoxCnt=14
# 00:21:00

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    graph = [[0] * n for _ in range(n)]
    num = 1
    drc = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    r, c, d = 0, -1, 0
    while num <= n ** 2:
        dr, dc = drc[d]
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n and graph[nr][nc] == 0:
            graph[nr][nc] = num
            r, c = nr, nc
            num += 1
        else:
            d = (d + 1) % 4

    print("#{0}".format(test_case))
    for row in graph:
        print(" ".join(map(str, row)))
