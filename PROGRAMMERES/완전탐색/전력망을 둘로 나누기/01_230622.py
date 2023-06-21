import collections


def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def check(wires, n):
    parent = [i for i in range(n + 1)]
    for a, b in wires:
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
    sub = [find_parent(parent, i) for i in range(1, n + 1)]
    subCnt = set(sub)

    if len(subCnt) > 2:
        return n
    s1, s2 = subCnt
    return abs(sub.count(s1) - sub.count(s2))


def solution(n, wires):
    wires = collections.deque(wires)
    answer = n
    for i in range(n):
        w = wires.popleft()
        answer = min(check(wires, n), answer)
        wires.append(w)
    return answer