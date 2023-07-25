def solution(picks, minerals):
    [dia, iron, stone] = picks
    score = []
    picks_cnt = dia + iron + stone

    for i in range(0, min(len(minerals), picks_cnt * 5), 5):
        m = minerals[i:i + 5]
        d = m.count("diamond")
        i = m.count("iron")
        s = m.count("stone")
        score.append((25 * d + 5 * i + s, d, i, s))
    score.sort(reverse=True)
    answer = sum([d + i + s for [t, d, i, s] in score[0:dia]])
    for [t, d, i, s] in score[dia:dia + iron]:
        answer += (d * 5 + i + s)
    for [t, d, i, s] in score[dia + iron:dia + iron + stone]:
        answer += (d * 25 + i * 5 + s)
    return answer
