import collections


def popQueue(q, cap):
    cnt = 0
    while cnt <= cap and len(q) > 0:
        d = q.pop()
        cnt += d
    if cnt > cap:
        q.append(cnt - cap)
    return q


def removeEmpty(q):
    while len(q) > 0 and q[-1] == 0:
        q.pop()
    return q


def solution(cap, n, deliveries, pickups):
    cnt = 0
    pt, dt = 0, 0
    deliveries = collections.deque(deliveries)
    pickups = collections.deque(pickups)
    deliveries = removeEmpty(deliveries)
    pickups = removeEmpty(pickups)
    while len(pickups) > 0 or len(deliveries) > 0:
        p = len(pickups)
        d = len(deliveries)
        dis = max(p, d)
        cnt += dis * 2
        if len(deliveries) > 0:
            deliveries = popQueue(deliveries, cap)
        if len(pickups) > 0:
            pickups = popQueue(pickups, cap)
    return cnt