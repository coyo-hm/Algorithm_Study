def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if findDivisor(i) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer

def findDivisor(num):
    return len([i for i in range(1, num + 1) if num % i == 0])