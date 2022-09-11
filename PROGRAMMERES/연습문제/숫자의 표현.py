def solution(n):
    answer = 1
    for start in range(1, n // 2 + 1):
        for end in range(start + 1, n // 2 + 3):
            if sum(range(start, end)) == n:
                answer += 1
                break
            if sum(range(start, end)) > n:
                break
    return answer
