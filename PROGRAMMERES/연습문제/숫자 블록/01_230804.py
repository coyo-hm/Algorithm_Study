def find(n):
    if n == 1:
        return 0
    d = [1]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0 and i <= 1e7:
            d.append(i)
            if n // i <= 1e7 and n // i != n:
                d.append(n // i)
    return max(d)


def solution(begin, end):
    answer = []

    for n in range(begin, end + 1):
        answer.append(find(n))
    return answer