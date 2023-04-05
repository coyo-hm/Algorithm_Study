from collections import deque

def diff(word, target):
    cnt = 0
    for i in range(len(word)):
        if word[i] != target[i]:
            if cnt + 1 > 1:
                return False
            cnt += 1
    return True

def solution(begin, target, words):
    q = deque([(begin, 0)])
    visited = [False] * len(words)

    while q:
        w, cnt = q.popleft()
        if w == target:
            return cnt
        for i in range(len(words)):
            if visited[i] == False and diff(w, words[i]):
                q.append((words[i], cnt + 1))
                visited[i] = True
    return 0