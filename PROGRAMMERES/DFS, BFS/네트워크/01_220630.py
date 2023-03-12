import collections
def solution(n, computers):
    v = [0] * (n)
    answer = 0
    for i in range(n):
        if v[i] == 0:
            answer += 1
            DFS(i, computers, v)

    return answer

def DFS(n, computers, v):
    v[n] = 1
    for i in range(len(computers[n])):
        if i != n and computers[n][i] == 1 and v[i] == 0:
            DFS(i, computers, v)