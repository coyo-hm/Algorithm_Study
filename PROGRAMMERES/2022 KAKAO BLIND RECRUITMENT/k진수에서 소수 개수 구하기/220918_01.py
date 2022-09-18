def changeNum(n, k):
    N = ""
    while n >= 1:
        N = str(n % k) + N
        n = n // k
    return N

def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
    
def solution(n, k):
    s = changeNum(n, k)
    p = [int(i) for i in s.split("0") if len(i) > 0 and int(i) != 1]
    answer = 0
    for i in p:
        if(isPrime(i)):
            answer += 1
    
    return answer 

