import collections


def solution(prices):
    q = collections.deque(prices)
    answer = []

    while q:
        p = q.popleft()
        time = 0
        for i in q:
            time += 1
            if i < p:
                break;
        answer.append(time)

    return answer