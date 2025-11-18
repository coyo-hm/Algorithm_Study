# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV5Pq-OKAVYDFAUq&probBoxId=AV9oaSMa3DEDFAQc&type=PROBLEM&problemBoxTitle=%5BD1%7ED2+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part2&problemBoxCnt=14
# 00:10:53

def rotate(graph, n):
    rotated_graph = []
    for c in range(n):
        row = []
        for r in range(n - 1, -1, -1):
            row.append(graph[r][c])
        rotated_graph.append(row)
    return rotated_graph


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    deg90 = rotate(graph, n)
    deg180 = rotate(deg90, n)
    deg270 = rotate(deg180, n)
    print("#{0}".format(test_case))
    for r in range(n):
        print("".join(map(str, deg90[r])), "".join(map(str, deg180[r])), "".join(map(str, deg270[r])))
