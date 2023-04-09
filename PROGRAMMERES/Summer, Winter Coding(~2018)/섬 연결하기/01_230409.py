#특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    #루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

#두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(v, costs):
    answer = 0
    edges = []
    for c in costs:
        [n1, n2, cost] = c
        edges.append((cost, n1, n2))

    edges.sort()
    parent = [0] * (v + 1)

    for i in range(1, v + 1):
        parent[i] = i

    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += cost


    return answer