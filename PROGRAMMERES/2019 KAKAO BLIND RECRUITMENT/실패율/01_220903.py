def solution(N, stages):
    person = len(stages)
    failure_rate = []
    for i in range(N + 1):
        cnt = stages.count(i + 1)
        failure_rate.append((cnt / person if cnt != 0 else 0, i + 1))
        person -= cnt
    failure_rate = sorted(failure_rate, key = lambda x: (-x[0], x[1]))
    return [i[1] for i in failure_rate if i[1] < N + 1]