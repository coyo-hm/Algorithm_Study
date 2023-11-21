from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

def check(graph, person):
    p = len(person)
    for i in range(p):
        [sr, sc] = person[i]
        q = deque([(sr, sc)])
        distance = [[int(1e9)] * 5 for _ in range(5)]
        visited = [[False] * 5 for _ in range(5)]
        visited[sr][sc] = True
        distance[sr][sc] = 0
        while q:
            r, c = q.popleft()
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < 5 and 0 <= nc < 5 and graph[nr][nc] != "X" and visited[nr][nc] == False:
                    distance[nr][nc] = distance[r][c] + 1
                    q.append((nr, nc))
                    visited[nr][nc] = True
        for j in range(i + 1, p):
            [r, c] = person[j]
            if distance[r][c] <= 2:
                return 0
    return 1

def solution(places):
    answer = []
    for graph in places:
        person = []
        graph = [list(row) for row in graph]
        for r in range(5):
            for c in range(5):
                if graph[r][c] == "P":
                    person.append((r, c))
        answer.append(check(graph, person))
    return answer