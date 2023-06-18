import collections
def solution(order):
    sub = collections.deque([])
    order = collections.deque(order)
    answer, i = 0, 1
    while order:
        o = order.popleft()
        if len(sub) > 0 and sub[-1] == o:
            answer += 1
            sub.pop()
        elif i < o:
            sub.extend(list(range(i, o)))
            answer += 1
            i = o + 1
        elif i > o:
            return answer
        elif i == o:
            i += 1
            answer += 1
    return answer