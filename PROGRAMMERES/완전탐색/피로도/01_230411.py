import itertools

def solution(k, dungeons):
    answer = 0
    dl = len(dungeons)

    for order in itertools.permutations(dungeons, dl):
        temp = k
        cnt = 0
        for d in order:
            minP, minusP = d
            if minP <= temp:
                cnt += 1
                temp -= minusP
        if answer < cnt:
            answer = cnt

    return answer