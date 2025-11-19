# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV139KOaABgCFAYh&probBoxId=AV-HZfeqN3ADFASP&type=PROBLEM&problemBoxTitle=%5BD2%7ED3+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part3&problemBoxCnt=14
# 00:21:50


import heapq

for test_case in range(1, 11):
    count = int(input())
    graph = list(map(int, input().split()))
    min_graph = graph.copy()
    max_graph = [-1 * g for g in graph]
    heapq.heapify(min_graph)
    heapq.heapify(max_graph)
    for _ in range(count):
        min_n = heapq.heappop(min_graph)
        heapq.heappush(min_graph, min_n + 1)
        max_n = heapq.heappop(max_graph)
        heapq.heappush(max_graph, max_n + 1)

    answer = (-1) * heapq.heappop(max_graph) - heapq.heappop(min_graph)

    print("#{0}".format(test_case), answer)
