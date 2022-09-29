from itertools import combinations
def solution(numbers, target):
    answer = 0
    s = sum(numbers)
    for minus in range(len(numbers)):
        m_nums = list(combinations(numbers, minus))
        for m in m_nums:
            if s - 2 * sum(m) == target:
                answer += 1              
    return answer