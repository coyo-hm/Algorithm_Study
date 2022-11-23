def solution(N, stages):
    stage = [[0, i] for i in range(1, N + 2)]
    for i in stages:
        stage[i - 1][0] += 1
    total = len(stages)
    for i in range(N):
        score, idx = stage[i]
        stage[idx - 1][0] = score / total if total != 0 else 0
        total -= score
    
    res=sorted(stage[:-1], key = lambda x: (-x[0], x[1]))
    return [idx for score, idx in res]