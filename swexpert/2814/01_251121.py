# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV7GOPPaAeMDFAXB&probBoxId=AV6kld8aiskDFASb&type=PROBLEM&problemBoxTitle=%EC%82%BC%EC%84%B1%EC%8B%9C%ED%97%98%EB%8C%80%EB%B9%84+%EA%B8%B0%EB%B3%B8%EB%AC%B8%EC%A0%9C%EB%AA%A8%EC%9D%8C%28%EB%82%9C%EC%9D%B4%EB%8F%84+1%7E3%29&problemBoxCnt=15
# 01:07:28

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    adj = [[] for _ in range(N + 1)]
    distance = 1
    for _ in range(M):
        x, y = map(int, input().split())
        adj[x].append(y)
        adj[y].append(x)


    def dfs(curr_node, curr_distance, visited):
        global distance
        if distance < curr_distance:
            distance = curr_distance
        for node in adj[curr_node]:
            if not visited[node]:
                visited[node] = True
                dfs(node, curr_distance + 1, visited)
                visited[node] = False


    for start_node in range(1, N + 1):
        visited = [False] * (N + 1)
        visited[start_node] = True
        dfs(start_node, 1, visited)

    print("#{0}".format(test_case), distance)
