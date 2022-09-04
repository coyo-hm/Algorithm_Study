def solution(sizes):
    sizes = [[max(x), min(x)] for x in sizes]
    return max([x[0] for x in sizes]) * max([x[1] for x in sizes])