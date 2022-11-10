from itertools import permutations 

def solution(n, weak, dist):
    l = len(weak)
    answer = len(dist) + 1
    for i in range(l):
        weak.append(n + weak[i])
    for start in range(l):
        for friends in list(permutations(dist, len(dist))):
            cnt = 1
            p = weak[start] + friends[cnt - 1]
            for i in range(start, start + l):
                if weak[i] > p:
                    cnt += 1
                    if cnt > len(dist):
                        break
                    p = weak[i] + friends[cnt - 1]
            answer = min(answer, cnt)
    return answer if answer <= len(dist) else -1