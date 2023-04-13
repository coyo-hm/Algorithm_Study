import heapq

INF = int(1e9)

def dij(graph, s, n):
    distance = [INF] * (n + 1)
    q = [(0, s)]
    heapq.heapify(q)
    distance[s] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance


def solution(n, s, a, b, fares):
    answer = INF
    graph = [[] for i in range(n + 1)]

    for fare in fares:
        c, d, f = fare
        graph[c].append((d, f))
        graph[d].append((c, f))

    dis_s = dij(graph, s, n)
    dis_a = dij(graph, a, n)
    dis_b = dij(graph, b, n)


    for k in range(1, n + 1):
        answer = min(answer, dis_s[k] + dis_a[k] + dis_b[k])

    return answer