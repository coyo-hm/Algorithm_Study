def Collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return n * 3 + 1

def solution(num):
    answer = 0
    while(num != 1):
        if answer >= 500:
            return -1
        num = Collatz(num)
        answer += 1
    
    return answer