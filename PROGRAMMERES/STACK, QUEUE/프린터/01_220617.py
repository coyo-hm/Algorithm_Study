import collections


def solution(priorities, location):
    pri = collections.deque([[i, priorities[i]] for i in range(len(priorities))])
    answer = 0
    while pri:
        p = pri.popleft()
        maxP = p[1]
        for i in pri:
            maxP = max(maxP, i[1])
        if (maxP != p[1]):
            pri.append(p)
        else:
            answer += 1
            if (p[0] == location): break

    return answer