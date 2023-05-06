def solution(n, cores):
    if n <= len(cores):
        return n
    n -= len(cores)
    start, end = 0, max(cores) * n
    while start < end:
        mid = (start + end) // 2
        work = 0
        for i in range(len(cores)):
            work += mid // cores[i]
        if work >= n:
            end = mid
        else:
            start = mid + 1

    for c in cores:
        n -= (end - 1) // c

    for i in range(len(cores)):
        if end % cores[i] == 0:
            n -= 1
            if n == 0:
                return i + 1