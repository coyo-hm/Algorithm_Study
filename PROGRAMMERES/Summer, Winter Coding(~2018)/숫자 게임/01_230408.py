import collections

def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    A = collections.deque(A)
    B = collections.deque(B)

    while A and B:
        a = A.popleft()
        b = B.popleft()
        while b <= a and B:
            b = B.popleft()
        if b > a:
            answer += 1

    return answer