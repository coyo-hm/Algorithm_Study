def solution(sequence, k):
    sl = len(sequence)
    answer = []
    t = sequence[0]
    e = 0

    for s in range(sl):
        while e + 1 < sl and t < k:
            e += 1
            t += sequence[e]

        if t == k:
            if not answer:
                answer = [s, e]
            else:
                if e - s < answer[1] - answer[0]:
                    answer = [s, e]

        t -= sequence[s]
    return answer