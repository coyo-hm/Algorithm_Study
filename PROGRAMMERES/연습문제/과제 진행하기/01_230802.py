import collections


def calcTime(time):
    [h, m] = time.split(":")
    return int(h) * 60 + int(m)


def solution(plans):
    plans.sort(key=lambda x: (calcTime(x[1])))
    answer = []
    q = collections.deque([])
    now = plans[0]
    for i in range(1, len(plans)):
        # print(plans[i], now, q)
        [name, start, playtime] = plans[i]
        nowS = calcTime(start)
        prevS = calcTime(now[1]) + int(now[2])
        playtime = int(playtime)
        if prevS <= nowS:
            answer.append(now[0])
            while prevS <= nowS and len(q) > 0:
                n = q[-1]
                if n[1] + prevS <= nowS:
                    answer.append(n[0])
                    q.pop()
                else:
                    q[-1] = [n[0], n[1] + prevS - nowS]
                prevS += n[1]
        else:
            q.append([now[0], prevS - nowS])
        now = plans[i]

    answer.append(now[0])

    while q:
        n = q.pop()
        answer.append(n[0])
    return answer