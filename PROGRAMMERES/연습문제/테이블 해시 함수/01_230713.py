# https://school.programmers.co.kr/learn/courses/30/lessons/147354

def solution(data, col, row_begin, row_end):
    si = []
    data.sort(key = lambda x: (x[col - 1], -x[0]))
    ans = 0
    for i in range(row_begin - 1, row_end):
        ans ^= sum([c % (i + 1) for c in data[i]])
    return ans