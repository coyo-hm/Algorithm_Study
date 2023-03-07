def solution(k, tangerine):
    answer = 0
    tan = [[0, i] for i in range(max(tangerine) + 1)]
    for t in tangerine:
        tan[t][0] += 1

    tan.sort(reverse = True)
    total = 0
    while total < k:
        total += tan[answer][0]
        answer += 1
    return answer